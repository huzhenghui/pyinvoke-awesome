from invoke import task
import django

@task
def get_version(c):
    print(django.get_version())