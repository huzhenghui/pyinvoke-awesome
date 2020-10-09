from invoke import task
import sys

@task
def install_django(c):
    # To avoid this problem you can invoke Python with '-m pip' instead of running pip directly.
    c.run(sys.executable + " -m pip install Django")

@task
def django_version(c):
    c.run(sys.executable + " -m django --version")
