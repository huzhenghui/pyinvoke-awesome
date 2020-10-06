from invoke import task, Responder

@task
def auto_pick(c):
    boy = Responder(
        pattern=r"boy",
        response="Tom\n"
    )
    girl = Responder(
        pattern=r"girl",
        response="Alice\n"
    )
    c.run("echo boy; read answer; echo $answer; echo girl; read answer; echo $answer", watchers=[boy, girl])
    c.run("echo girl; read answer; echo $answer; echo boy; read answer; echo $answer", watchers=[boy, girl])