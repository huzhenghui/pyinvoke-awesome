from invoke import task

@task
def caller(c):
    print("caller")
    callee(c)

@task
def callee(c):
    print("callee")