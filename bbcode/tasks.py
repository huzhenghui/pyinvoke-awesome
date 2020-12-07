import sys
from invoke import task
from invoke.context import Context
import bbcode


@task
def install_bbcode(c):
    c.run(sys.executable + " -m pip install bbcode")


@task
def bbcode_render_html(c):
    print(bbcode.render_html(sys.stdin.read()))


@task
def bbcode_parser_format(c):
    parser = bbcode.Parser()
    parser.add_simple_formatter('u', '<strong>%(value)s</strong>')
    parser.add_simple_formatter('color', '%(value)s')
    print(parser.format(sys.stdin.read()))


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
