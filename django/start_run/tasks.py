from invoke import task, Context
import sys
import webbrowser
from django.core.management import ManagementUtility

site_name = "my_site_name"
port = 8080

@task
def startproject(c):
    utility = ManagementUtility(["django-admin", "startproject", site_name])
    utility.execute()

@task
def runserver(c):
    runserver_internal(c)

def runserver_internal(c: Context):
    with c.cd(site_name):
        c.run(sys.executable + " manage.py runserver " + str(port))

@task
def browser(c):
    webbrowser.open("http://127.0.0.1:" + str(port))