from invoke import task

# ln -s "../$(dirname $(git ls-files --directory --full-name ./lib_sub_directory/sub_directory_lib.py))" "$(git root)/typings/"
from lib_sub_directory.sub_directory_lib import sub_directory_function


@task
def caller(c):
    print("caller")
    callee(c)


@task
def callee(c):
    print("callee")
    sub_directory_function()
