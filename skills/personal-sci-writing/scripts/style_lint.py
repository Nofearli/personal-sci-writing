"""Deterministic personal-style lint for .md/.txt/.tex, Python 3 stdlib only.

Masks protected material without changing offsets. This is a conservative LaTeX
lexer, not a TeX engine. Custom macros and verbatim syntaxes need explicit spans
or style-lint: off/on markers. Never auto-rewrites source.
"""
import argparse
import collections
import json
import re
import sys
from pathlib import Path

DEFAULT_RULES = Path(__file__).resolve().parents[1]/'language-rules.json'


def _blank(text):
    return ''.join('\n' if c=='\n' else ' ' for c in text)


def _mask_pattern(text, pattern, flags=0, group=0):
    chars=list(text)
    for m in re.finditer(pattern,text,flags):
        a,b=m.span(group)
        chars[a:b]=_blank(text[a:b])
    return ''.join(chars)


def _group_end(text, start, opening='{', closing='}'):
    if start>=len(text) or text[start]!=opening:return start
    depth=1;i=start+1
    while i<len(text):
        if text[i]=='\\':i+=2;continue
        if text[i]==opening:depth+=1
        if text[i]==closing:depth-=1
        i+=1
        if depth==0:return i
    return len(text)


def mask_protected(text, suffix, rules):
    # Explicit markers work in plain text, Markdown comments, and LaTeX comments.
    text=_mask_pattern(text,r'[^\n]*style-lint:\s*off\b.*?(?:[^\n]*style-lint:\s*on\b[^\n]*|\Z)',re.I|re.S)
    for literal in rules.get('allowed_literal_spans',[]):
        text=_mask_pattern(text,re.escape(literal))
    if suffix.lower() in ['.md','.markdown']:
        text=_mask_pattern(text,r'\A---\s*\n.*?\n---[^\n]*',re.S)
        text=_mask_pattern(text,r'(?ms)^[ \t]*(`{3,}|~{3,})[^\n]*\n.*?^[ \t]*\1[^\n]*(?:\n|$)')
        text=_mask_pattern(text,r'`+[^`\n]*`+')
        text=_mask_pattern(text,r'(?m)^\s*>[^\n]*(?:\n[ \t]*>[^\n]*)*')
        text=_mask_pattern(text,r'<!--.*?-->',re.S)
        text=_mask_pattern(text,r'\[[^\]]*\]\(([^)]+)\)',group=1)
        text=_mask_pattern(text,r'(?mi)^(#{1,6})\s+(?:references|bibliography)\b[^\n]*\n.*?(?=^#{1,6}\s|\Z)',re.S)
    if suffix.lower() in ['.tex','.latex']:
        # Remove comments first, respecting escaped percent.
        chars=list(text)
        for m in re.finditer('%',text):
            i=m.start();n=0;j=i-1
            while j>=0 and text[j]=='\\':n+=1;j-=1
            if n%2==0:
                end=text.find('\n',i)
                if end<0:end=len(text)
                chars[i:end]=_blank(text[i:end])
        text=''.join(chars)
        begin=re.search(r'\\begin\s*\{document\}',text)
        if begin:text=_blank(text[:begin.end()])+text[begin.end():]
        text=_mask_pattern(text,r'\\(?:verb\*?)([^\w\s]).*?\1')
        envs=r'equation\*?|align\*?|alignat\*?|gather\*?|multline\*?|displaymath|math|eqnarray\*?|thebibliography|verbatim\*?|lstlisting|minted|quote|quotation|filecontents\*?|tikzpicture'
        text=_mask_pattern(text,rf'\\begin\s*\{{({envs})\}}.*?\\end\s*\{{\1\}}',re.S)
        text=_mask_pattern(text,r'\\(?:section|chapter)\*?\s*\{(?:References|Bibliography)\}.*?(?=\\(?:section|chapter)\*?\s*\{|\\end\s*\{document\}|\Z)',re.I|re.S)
        # Commands whose arguments are identifiers, metadata, citations or exact quotes.
        skip={'cite','citep','citet','citealp','citeauthor','citeyear','ref','eqref','autoref','cref','Cref','label','url','path','includegraphics','bibliographystyle','addbibresource','input','include','title','author','thanks','affiliation','address','email','enquote','foreignquote','lstinline','bibliography','nocite','index','glossary','vspace','hspace','setlength','documentclass','usepackage'}
        chars=list(text)
        for m in re.finditer(r'\\([A-Za-z]+)\*?',text):
            name=m.group(1);pos=m.end()
            if name in ['newcommand','renewcommand','providecommand','DeclareRobustCommand','def','newenvironment','renewenvironment','newtheorem','DeclareMathOperator']:
                # Mask macro declaration and all following balanced argument groups.
                while pos<len(text) and text[pos].isspace():pos+=1
                if pos<len(text) and text[pos]=='\\':
                    mm=re.match(r'\\[A-Za-z]+',text[pos:]);pos+=len(mm.group()) if mm else 1
                if name=='def':
                    group=text.find('{',pos)
                    if group>=0:pos=_group_end(text,group)
                    chars[m.start():pos]=_blank(text[m.start():pos]);continue
                for _ in range(5):
                    while pos<len(text) and text[pos].isspace():pos+=1
                    if pos<len(text) and text[pos] in '{[':
                        pos=_group_end(text,pos,text[pos],'}' if text[pos]=='{' else ']')
                    else:break
                chars[m.start():pos]=_blank(text[m.start():pos]);continue
            if name not in skip and name!='href':continue
            end=pos
            while end<len(text):
                p=end
                while p<len(text) and text[p].isspace():p+=1
                if p<len(text) and text[p]=='[':end=_group_end(text,p,'[',']');continue
                if p<len(text) and text[p]=='{':end=_group_end(text,p);break
                break
            chars[m.start():end]=_blank(text[m.start():end])
        text=''.join(chars)
    # Math in all three input formats, including Markdown inline LaTeX.
    text=_mask_pattern(text,r'\\\[.*?\\\]|\\\(.*?\\\)',re.S)
    text=_mask_pattern(text,r'(?<!\\)\$\$.*?(?<!\\)\$\$',re.S)
    text=_mask_pattern(text,r'(?<!\\)\$(?!\$).*?(?<!\\)\$',re.S)
    text=_mask_pattern(text,r'https?://[^\s<>]+')
    if rules.get('exclude_quoted_strings',True):
        # Quoted prose is protected evidence. Use explicit markers for other quote conventions.
        text=_mask_pattern(text,r'"[^"\n]*"|“[^”]*”|``.*?\'\'',re.S)
    if suffix.lower() in ['.tex','.latex']:
        # Keep visible arguments of formatting commands, discard command names.
        text=_mask_pattern(text,r'\\(?:begin|end)\s*\{[^}]+\}')
        text=_mask_pattern(text,r'\\(?:[A-Za-z]+\*?|[^A-Za-z\s])')
    return text


def sentence_spans(text):
    buf=list(text)
    for m in re.finditer(r'\b(?:Fig|Figs|Eq|Eqs|Sec|Dr|Prof|Th)\.|\bi\.e\.|\be\.g\.|\bet al\.|(?<=\d)\.(?=\d)',text,re.I):
        for i in range(m.start(),m.end()):
            if buf[i]=='.':buf[i]='\u2024'
    protected=''.join(buf);start=0
    for m in re.finditer(r'[.!?](?=\s|$)|\n\s*\n',protected):
        end=m.end()
        if text[start:end].strip():yield start,end
        start=end
    if text[start:].strip():yield start,len(text)


def expression_pattern(expression):
    # Exact lexical form, case-insensitive, flexible whitespace between phrase words.
    return r'(?<!\w)'+r'\s+'.join(re.escape(w) for w in expression.split())+r'(?!\w)'


def lint_text(text, filename, rules=None):
    rules=rules or json.loads(DEFAULT_RULES.read_text(encoding='utf-8'))
    visible=mask_protected(text,Path(filename).suffix,rules)
    issues=[]
    def add(pos,category,rule,match,suggestion,severity='error'):
        issues.append(dict(file=str(filename),line=text.count('\n',0,pos)+1,column=pos-(text.rfind('\n',0,pos)+1)+1,category=category,rule=rule,match=match,suggestion=suggestion,severity=severity))
    for field,category in [('banned_expressions','banned-expression'),('first_person','first-person'),('soft_expressions','preference')]:
        for exp in rules.get(field,[]):
            for m in re.finditer(expression_pattern(exp),visible,re.I):
                suggestion='Restructure this clause using the section phrase bank, preserving conditions and technical meaning.'
                if field=='first_person':suggestion='Use a method/result subject or a grammatical passive construction.'
                add(m.start(),category,exp,text[m.start():m.end()],suggestion,'warning' if field=='soft_expressions' else 'error')
    for exp in rules.get('banned_punctuation',[]):
        for m in re.finditer(re.escape(exp),visible):
            add(m.start(),'punctuation',exp,exp,'Split into complete sentences or restructure with an explicit logical relation.')
    openings=collections.defaultdict(list)
    for a,b in sentence_spans(visible):
        ww=list(re.finditer(r"[A-Za-z]+(?:[-’'][A-Za-z]+)*",visible[a:b]))
        if not ww:continue
        pos=a+ww[0].start()
        if len(ww)>rules['max_sentence_words']:
            add(pos,'long-sentence',f"max_sentence_words={rules['max_sentence_words']}",str(len(ww)), 'Review whether separate claims can be split without losing scope. This is an advisory threshold.','warning')
        k=rules['repeated_opening_words']
        if len(ww)>=k:
            key=' '.join(w.group().lower() for w in ww[:k])
            openings[key].append(pos)
    for key,positions in openings.items():
        if len(positions)>=rules['repeated_opening_threshold']:
            for pos in positions:
                add(pos,'repeated-opening',f"opening_occurrences={len(positions)}",key,'Vary sentence focus when useful. Do not replace necessary technical terminology.','warning')
    return sorted(issues,key=lambda x:(x['line'],x['column'],x['category']))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('files',nargs='+',type=Path)
    p.add_argument('--rules',type=Path,default=DEFAULT_RULES)
    p.add_argument('--format',choices=['text','json'],default='text')
    p.add_argument('--output',type=Path)
    p.add_argument('--fail-on',choices=['error','warning','none'],default='error')
    args=p.parse_args()
    try:
        rules=json.loads(args.rules.read_text(encoding='utf-8'))
        findings=[]
        for path in args.files:
            findings.extend(lint_text(path.read_text(encoding='utf-8-sig'),path,rules))
    except (OSError,ValueError,KeyError) as exc:
        print(str(exc),file=sys.stderr);return 2
    if args.format=='json':output=json.dumps(findings,ensure_ascii=False,indent=2)
    else:output='\n'.join(f"{i['file']}:{i['line']}:{i['column']}: {i['severity']} [{i['category']}] {i['rule']} -> {i['suggestion']}" for i in findings) or 'No style issues detected in scanned prose.'
    if args.output:args.output.write_text(output+'\n',encoding='utf-8')
    else:print(output)
    return int(args.fail_on!='none' and any(args.fail_on=='warning' or i['severity']=='error' for i in findings))


if __name__=='__main__':
    raise SystemExit(main())
