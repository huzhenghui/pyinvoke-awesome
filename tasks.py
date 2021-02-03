from invoke import task
import json
import os
import platform
import sys


@task
def invoke_choose(c):
    result = c.run(
        "invoke --list --list-format=json | jq '.tasks[].name' | /usr/local/opt/choose-gui/bin/choose")
    print("\nChoose Recipe: ", result.stdout)
    c.run("invoke " + result.stdout)


@task
def invoke_fzf(c):
    result = c.run(
        'pwsh -c "invoke --list --list-format=json | ConvertFrom-Json | Select-Object -ExpandProperty tasks | Select-Object -ExpandProperty name | fzf"')
    print("\nChoose Recipe: ", result.stdout)
    c.run("invoke " + result.stdout)


@task
def unknown_os(c):
    print("Unknown OS : ", platform.system())


@task(default=True)
def default_task(c):
    os_default = {
        'Darwin': invoke_choose,
        'Windows': invoke_fzf
    }
    os_default.get(platform.system(), unknown_os)(c)


@task
def invoke_list(c):
    c.run("invoke --list")


@task
def invoke_list_nested(c):
    c.run("invoke --list --list-format=nested")


@task
def invoke_list_json(c):
    c.run("invoke --list --list-format=json")


def get_pyinvoke_draft_dir(c):
    result = c.run("jump cd pyinvoke-draft")
    return result.stdout


@task
def pyinvoke_draft_dir(c):
    print(get_pyinvoke_draft_dir(c))


@task
def code(c):
    cwd = os.getcwd()
    workspace = cwd + "/pyinvoke.code-workspace"
    if os.path.exists(workspace):
        c.run("code " + workspace)
    else:
        c.run("code " + cwd)


@task
def executable(c):
    print(sys.executable)


@task
def vscode_settings(c):
    settings = {
        "python.pythonPath": sys.executable
    }
    print(json.dumps(settings))
