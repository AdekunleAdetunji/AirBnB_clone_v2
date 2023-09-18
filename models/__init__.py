#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv


st_type = getenv("HBNB_TYPE_STORAGE")
storage = FileStorage() if st_type == "file" else DBStorage()
storage.reload()
