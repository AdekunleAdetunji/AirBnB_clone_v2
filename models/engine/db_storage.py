#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import IntegrityError
from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User

class_map = {
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'State': State,
    'Review': Review,
    'User': User
}


class DBStorage:
    """class representing database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """initiallizes a DBStorage instance"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, db),
            pool_pre_ping=True)
        if env == "test":
            Base.metadata.dropall(self.__engine)

    def all(self, cls=None):
        """fetches all items from db"""
        items = []
        result = {}
        if cls:
            if type(cls) is str:
                cls = class_map.get(cls, None)
            items = self.__session.query(cls)
        else:
            for c in class_map.values():
                items += self.__session.query(c)
        for obj in items:
            if hasattr(obj, '_sa_instance_state'):
                delattr(obj, '_sa_instance_state')
            key = f"{type(obj).__name__}.{obj.id}"
            result[key] = obj
        return result

    def new(self, obj):
        """adds a new item to the db session"""
        if not obj:
            return
        try:
            self.__session.add(obj)
        except Exception as e:
            print(e.message)

    def save(self):
        """persists session to db"""
        try:
            self.__session.commit()
        except IntegrityError as e:
            print(e._sql_message)

    def reload(self):
        """reloads the db"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

    def delete(self, obj=None):
        """deletes an object from db"""
        if obj:
            self.__session.delete(obj)
