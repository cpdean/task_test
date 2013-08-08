from fabric.api import task

import main

@task
def task1():
    c = main.Corpus()
    print c.__class__.__name__

