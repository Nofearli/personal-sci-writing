import importlib.util
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('style_lint',ROOT/'scripts/style_lint.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
RULES=json.loads((ROOT/'language-rules.json').read_text(encoding='utf-8'))


class StyleLintTests(unittest.TestCase):
    def lint(self,text,suffix='.txt',rules=None):return mod.lint_text(text,'sample'+suffix,rules or RULES)
    def test_exact_forms(self):
        issues=self.lint('WHICH while i.e. namely due to associated with corresponds we our us;')
        self.assertEqual(len(issues),11)
    def test_no_substrings(self):
        self.assertEqual(self.lint('Somewhere ourself user whiled corresponding due tonight.'),[])
    def test_phrase_newline_and_positions(self):
        issues=self.lint('The model is valid.\nThis changes due\nto wind.\nWe test it;')
        self.assertEqual([(i['line'],i['column'],i['rule']) for i in issues],[(2,14,'due to'),(4,1,'we'),(4,11,';')])
    def test_tex_visible_formatting(self):
        issues=self.lint(r'\section{Method} A \textbf{method which fails} is considered.','.tex')
        self.assertEqual([i['rule'] for i in issues],['which'])
    def test_tex_math_comments_refs(self):
        source=r'''\documentclass{which}
\newcommand{\which}[1]{while #1;}
\begin{document}
% we use this; which
$x_{which}; our$ and \(\text{we};\) and \[us;\]
\begin{align}which; we\end{align}
\cite[which]{while} \ref{our} \label{us} \url{https://x/which;}
The method is defined.
\begin{thebibliography}{9}\bibitem{a} Which method; our title.\end{thebibliography}
\end{document}'''
        self.assertEqual(self.lint(source,'.tex'),[])
    def test_tex_nested_metadata(self):
        self.assertEqual(self.lint(r'\author{We {which};} \title{Our {while};} The method is used.','.tex'),[])
    def test_tex_href_keeps_label(self):
        self.assertEqual([i['rule'] for i in self.lint(r'\href{https://a/which}{we investigate}','.tex')],['we'])
    def test_tex_comment_escaped_percent(self):
        self.assertEqual([i['rule'] for i in self.lint(r'10\% of our samples % which','.tex')],['our'])
    def test_tex_verbatim_quotes(self):
        self.assertEqual(self.lint(r'\verb|which;| \enquote{We {our};} \begin{quotation}while;\end{quotation}','.tex'),[])
    def test_markdown_protected(self):
        source='---\ntitle: Our paper;\n---\n> Which result;\n\n```tex\nwe which;\n```\n\n`our;` [method](https://x/which;) $x_{while};$\nThe model is valid.\n## References\nWe title;\n'
        self.assertEqual(self.lint(source,'.md'),[])
    def test_quotes_and_explicit_regions(self):
        self.assertEqual(self.lint('"which; our"\nstyle-lint: off\nwe; which\nstyle-lint: on\nThe model is considered.'),[])
    def test_configurable_names(self):
        rules={**RULES,'allowed_literal_spans':['Which Robot']}
        self.assertEqual(self.lint('Which Robot is tested.',rules=rules),[])
    def test_long_sentence_is_advisory(self):
        issues=self.lint(' '.join(['word']*46)+'.')
        self.assertEqual([(i['category'],i['severity']) for i in issues],[('long-sentence','warning')])
    def test_repetition(self):
        issues=self.lint('The proposed method is used for analysis. The proposed method is used for control. The proposed method is used for estimation.')
        self.assertEqual(sum(i['category']=='repeated-opening' for i in issues),3)
    def test_unclosed_math_conservative(self):
        # An unclosed delimiter does not suppress the remainder silently.
        self.assertEqual([i['rule'] for i in self.lint('$ unclosed which')],['which'])
    def test_no_regex_claims_about_voice(self):
        self.assertEqual(self.lint('The strategy guarantees stability. A controller is proposed.'),[])
    def test_bibliography_does_not_hide_appendix(self):
        issues=self.lint(r'\bibliography{our} \appendix \section{Proof} We prove this.','.tex')
        self.assertEqual([i['rule'] for i in issues],['we'])
    def test_markdown_references_stop_at_next_section(self):
        issues=self.lint('## References\nWhich title;\n## Appendix\nWe test this.','.md')
        self.assertEqual([i['rule'] for i in issues],['we'])
    def test_tex_reference_section_stops(self):
        issues=self.lint(r'\section*{References} Which title; \section{Appendix} Our result.','.tex')
        self.assertEqual([i['rule'] for i in issues],['our'])
    def test_custom_definitions_are_not_prose(self):
        issues=self.lint(r'\def\foo#1{which; #1} \newenvironment{test}{our;}{while} We investigate.','.tex')
        self.assertEqual([i['rule'] for i in issues],['we'])


if __name__=='__main__':unittest.main()
