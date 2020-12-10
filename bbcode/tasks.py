import sys
from invoke import task
from invoke.context import Context
import bbcode


@task
def install_bbcode(c):
    c.run(sys.executable + " -m pip install bbcode")


@task
def show_files_bbcode(c):
    context: Context = c
    context.run(sys.executable + " -m pip show --files bbcode")


@task
def inv_list(c):
    context: Context = c
    context.run('inv --list')


@task
def ghq_path(c):
    context: Context = c
    context.run(
        'echo "$(ghq list --full-path https://github.com/huzhenghui/pyinvoke-awesome)/bbcode"')


@task
def inv_ghq_root_list(c):
    context: Context = c
    context.run(
        'inv --search-root "$(ghq list --full-path https://github.com/huzhenghui/pyinvoke-awesome)/bbcode" --list')


@task
def bbcode_render_html(c):
    print(bbcode.render_html(sys.stdin.read()))


def bbcode_parser_formatter(data: str) -> str:
    parser = bbcode.Parser()
    parser.add_simple_formatter('u', '<strong>%(value)s</strong>')
    parser.add_simple_formatter('color', '%(value)s')
    parser.REPLACE_ESCAPE = (
        ("&", "&amp;"),
        ("<", "&lt;"),
        (">", "&gt;"),
        ('"', "&quot;"),
        ("'", "&#39;"),
        (" ", "&nbsp;"),
    )
    return parser.format(data)


@task
def bbcode_parser_format(c):
    print(bbcode_parser_formatter(sys.stdin.read()))


@task
def bbcode_parser_format_pre(c):
    print('<pre>' + bbcode_parser_formatter(sys.stdin.read()) + '</pre>')


@task
def bbcode_render_html_b(c):
    print(bbcode.render_html("[b]convert b to strong[/b]"))


@task
def bbcode_render_html_i(c):
    print(bbcode.render_html("[i]convert i to em[/i]"))


@task
def bbcode_render_html_u(c):
    print(bbcode.render_html("[u]convert u to u[/u]"))


@task
def bats_bbcode_html(c):
    context: Context = c
    context.run('trash ./TestReport/TestReport-bbcode-html.bats.xml', warn=True)
    context.run('trash ./TestReport/TestReport-bbcode-html.bats.html', warn=True)
    context.run(
        'bats --timing --formatter junit --output ./TestReport ./bbcode-html.bats', warn=True)
    context.run(
        'junit2html ./TestReport/TestReport-bbcode-html.bats.xml ./TestReport/TestReport-bbcode-html.bats.html')


@task
def bats_ansi_bbcode_html(c):
    context: Context = c
    context.run(
        'trash ./TestReport/TestReport-ansi-bbcode-html.bats.xml', warn=True)
    context.run(
        'trash ./TestReport/TestReport-ansi-bbcode-html.bats.html',  warn=True)
    context.run(
        'bats --timing --formatter junit --output ./TestReport ./ansi-bbcode-html.bats', warn=True)
    context.run(
        'junit2html ./TestReport/TestReport-ansi-bbcode-html.bats.xml ./TestReport/TestReport-ansi-bbcode-html.bats.html')


@task
def bats_ansi_bbcode_html_markdown(c):
    context: Context = c
    context.run(
        'trash ./TestReport/TestReport-ansi-bbcode-html-markdown.bats.xml', warn=True)
    context.run(
        'trash ./TestReport/TestReport-ansi-bbcode-html-markdown.bats.html', warn=True)
    context.run(
        'bats --timing --formatter junit --output ./TestReport ./ansi-bbcode-html-markdown.bats', warn=True)
    context.run('junit2html ./TestReport/TestReport-ansi-bbcode-html-markdown.bats.xml ./TestReport/TestReport-ansi-bbcode-html-markdown.bats.html')


@task
def sample_bold(c):
    context: Context = c
    context.run(
        'ack --help | ack --passthru --color --color-match="bold" "match"')


@task
def sample_bold_bbcode_html_markdown_ansi(c):
    context: Context = c
    context.run(
        'inv sample-bold | ansifilter --bbcode | inv bbcode-parser-format | pandoc --from=html --to=markdown | mdcat')


@task
def sample_italic(c):
    context: Context = c
    context.run(
        'ack --help | ack --passthru --color --color-match="italic" "match"')


@task
def sample_italic_bbcode_html_markdown_ansi(c):
    context: Context = c
    context.run(
        'inv sample-italic | ansifilter --bbcode | inv bbcode-parser-format | pandoc --from=html --to=markdown | mdcat')


@task
def sample_underline(c):
    context: Context = c
    context.run(
        'ack --help | ack --passthru --color --color-match="underline" "match"')


@task
def sample_underline_bbcode_html_markdown_ansi(c):
    context: Context = c
    context.run(
        'inv sample-underline | ansifilter --bbcode | inv bbcode-parser-format | pandoc --from=html --to=markdown | mdcat')


@task
def sample_inv_help(c):
    context: Context = c
    context.run(
        'inv --help | ugrep --color=always --colors="cx=HUwK;ms=nHUwK;mt=hu+r+Y" --any-line "STRING"')


@task
def sample_inv_help_bbcode_html_browser(c):
    context: Context = c
    context.run(
        'inv sample-inv-help | ansifilter --bbcode | inv bbcode-parser-format-pre | browser')


@task
def sample_inv_help_bbcode_html_markdown_ansi(c):
    context: Context = c
    context.run(
        'inv sample-inv-help | ansifilter --bbcode | inv bbcode-parser-format | pandoc --from=html --to=markdown | mdcat')
