__package__ = 'sibling_directory.main_directory'

from invoke import task

import sys_path_append  # type: ignore

from ..lib_sibling_directory.sibling_directory_lib import \
    sibling_directory_function


@task
def caller(c):
    print("caller")
    callee(c)


@task
def callee(c):
    print("callee")
    sibling_directory_function()
