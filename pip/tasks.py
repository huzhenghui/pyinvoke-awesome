from invoke import task
import sys

@task
def python_path(c):
    print(sys.executable)

@task
def pip(c):
    c.run(sys.executable + " -m pip")

@task
def pip_freeze(c):
    c.run(sys.executable + " -m pip freeze")

@task
def pip_list(c):
    c.run(sys.executable + " -m pip list")

@task
def pip_check(c):
    c.run(sys.executable + " -m pip check")

@task
def pip_debug(c):
    c.run(sys.executable + " -m pip debug")

@task
def pip_help(c):
    c.run(sys.executable + " -m pip help")

@task
def pip_version(c):
    c.run(sys.executable + " -m pip --version")
