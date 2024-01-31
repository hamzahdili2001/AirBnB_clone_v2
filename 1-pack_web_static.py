#!/usr/bin/python3
"""1-pack_web_static.py"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """Function do_pack"""
    try:
        if not os.path.exists("versions"):
            os.mkdir("versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        path = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(path))
        return path
    except Exception:
        return None
