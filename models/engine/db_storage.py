#!/usr/bin/python3
"""create New engine"""


from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        type_dict = {}
        query_classes = [User, State, City, Amenity, Place, Review]
        if cls:
            if cls in query_classes:
                query_classes = [cls]
            else:
                raise ValueError("Classe invalide: {}".format(cls))
        for query_class in query_classes:
            objects = self.__session.query(query_class).all()
            for obj in objects:
                key = "{}.{}".format(query_class.__name__, obj.id)
                type_dict[key] = obj
        return type_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Sec)
        self.__session = Session()
