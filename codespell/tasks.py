from invoke import task, Responder

@task
def check(c):
    c.run("codespell ./tasks.py")

@task
def codespell_help(c):
    c.run("codespell --help")

@task
def codespell_version(c):
    c.run("codespell --version")

@task
def calulated(c):
    c.run("echo fiel")
