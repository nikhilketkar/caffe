from fabric.operations import local as lrun, run
from fabric.api import task
from fabric.state import env
from fabric.api import settings
from fabric.context_managers import lcd

@task
def build():
    with settings(warn_only=True):
        lrun('mkdir build')
    with lcd('build'):
        lrun('cmake ..')
        lrun('make')
        lrun('make pycaffe')
    lrun('tar -czf caffe.tar.gz python')
