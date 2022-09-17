#!/usr/bin/python3
"""
Module send an archive to your web servers
"""
from os import *
from fabric.api import *
env.user = 'ubuntu'
env.hosts = ['35.229.20.253', '34.207.145.16']


def do_deploy(archive_path):
    """Send an archive to your web servers"""
    if archive_path is None:
        return False
    try:
        nfile = archive_path.split("/")[-1]
        npath = nfile.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, npath))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(nfile, path, npath))
        run('sudo rm /tmp/{}'.format(nfile))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(path, npath))
        run('sudo rm -rf {}{}/web_static'.format(path, npath))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}{}/ /data/web_static/current'.format(path, npath))
    except Exception:
        return False
    return True
