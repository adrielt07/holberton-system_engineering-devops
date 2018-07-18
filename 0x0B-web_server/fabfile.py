#!/usr/bin/python2.7
from fabric.api import run, hosts, local, put, env


env.user = "ubuntu"
env.password = ""
env.key_filename = "~/.ssh/holberton"


def pack():
    local("tar --exclude='*.tar.gz' -cvzf holbertonwebapp.tar.gz .")


def deploy():
    put("holbertonwebapp.tar.gz", "/tmp")
    run("mkdir /tmp/holbertonwebapp")
    run("tar -xvf /tmp/holbertonwebapp.tar.gz -C /tmp/holbertonwebapp")


def clean():
    local("rm holbertonwebapp.tar.gz")
