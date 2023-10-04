#!/usr/bin/python3
"""
This module contains a function that deploy web static files/folders to our
server"""

from fabric.api import *

do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy

env.hosts = ['ubuntu@3.90.82.95', 'ubuntu@54.157.156.207']


def deploy():
    """
    Function that create and distribute an archive to the listed archives
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
