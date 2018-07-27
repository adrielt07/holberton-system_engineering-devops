#!/usr/bin/python2.7
from fabric.api import run, hosts, local, put, env
from fabric.contrib import files

env.user = "ubuntu"
env.password = ""
env.key_filename = "~/.ssh/holberton"


def pack():
    local("tar --exclude='*.tar.gz' -cvzf holbertonwebapp.tar.gz .")


def deploy():
    put("holbertonwebapp.tar.gz", "/tmp")
    if files.exists("/tmp/holbertonwebapp") is False:
        run("mkdir /tmp/holbertonwebapp")
    run("tar -xvf /tmp/holbertonwebapp.tar.gz -C /tmp/holbertonwebapp")


def clean():
    local("rm holbertonwebapp.tar.gz")
