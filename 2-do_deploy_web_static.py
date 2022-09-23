#!/usr/bin/python3
"""a Fabric script (based on the file 1-pack_web_static.py)
    that distributes
    an archive to your web servers,
    using the function do_deploy:"""
from fabric.api import local, run, put
from fabric.api import env
from os.path import exists, isdir
import time
env.hosts = ['54.224.55.58']
env.user = 'ubuntu'
env.key = '~/.ssh/school'


def do_pack():
    """Funtion to generates the file"""

    if isdir('versions') is False:
        local("mkdir versions")
    file = "web_static_" + time.strftime("%Y%m%d%H%M%S", time.gmtime())\
        + ".tgz"
    result = local("tar -cvzf versions/{} web_static ".format(file))
    if result.failed:
        return None
    return result


def do_deploy(archive_path):
    """Funtion to distrubutes archives"""

    if exists(archive_path) is False:
        return False
    try:
        paths = archive_path.split("/")
        rute = paths[1].strip('.tgz')
        put("{}".format(archive_path), "/tmp/{}".format(paths[1]))
        run("mkdir -p /data/web_static/releases/{}/".format(rute))
        run("tar -xzf /tmp/{} -C\
            /data/web_static/releases/{}/".format(paths[1], rute))
        run("rm /tmp/{}".format(paths[1]))
        run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(rute, rute))
        run("rm -rf /data/web_static/releases/{}/web_static".format(rute))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/\
            /data/web_static/current".format(rute))
        return True
    except Exception:
        return False
