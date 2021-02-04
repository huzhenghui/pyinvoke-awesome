from invoke import task

# ln -s "../$(git ls-files --full-name ./same_directory_lib.py)" "$(git root)/typings/"
from same_directory_lib import same_directory_function


@task
def caller(c):
    print("caller")
    callee(c)


@task
def callee(c):
    print("callee")
    same_directory_function()
