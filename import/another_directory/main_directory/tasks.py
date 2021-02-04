from invoke import task

import sys_path_append  # type: ignore

# ln -s "../$(git ls-files --directory --full-name ../lib_another_directory/another_directory_lib.py)" "$(git root)/typings/"
from another_directory_lib import another_directory_function  # isort:skip


@task
def caller(c):
    print("caller")
    callee(c)


@task
def callee(c):
    print("callee")
    another_directory_function()
