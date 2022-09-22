#!/usr/bin/python3
"""
Module that contains script for make a package of the app and deploy it fully
"""
from fabric.api import *
from datetime import datetime
from os import path

do_pack = __import__('1-pack_web_static').do_pack


def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    """
    try:
        if not (path.exists(archive_path)):
            return False
        file_name = archive_path.split("/")[-1]
        ext_not = file_name.split(".")[0]
        rout_path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(rout_path, ext_not))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, rout_path, ext_not))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(rout_path, ext_not))
        run('rm -rf {}{}/web_static'.format(rout_path, ext_not))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(rout_path, ext_not))
    except Exception:
        return False
    return True


def deploy():
    """Function to deploy the app"""
    return do_deploy(do_pack())
