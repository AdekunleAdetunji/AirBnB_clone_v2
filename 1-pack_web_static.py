#!/usr/bin/python3
"""
This module contains a Fabric script that generates a .tgz
archive from the contents of the web_static folder of your AirBnB Clone repo,
 using the function do_pack
"""

import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    A function that is used to generate a tar file using the local function
    """
    if not os.path.exists("versions"):
        os.mkdir("versions")
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    filePath = f"versions/web_static_{time}.tgz"
    output = local(f"tar -cvzf {filePath} web_static")
    return filePath