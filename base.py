from sqlalchemy import *
from sqlalchemy_utils import *
from sqlalchemy.orm import *

username = input("username : ")
password = input("password : ")

path = "mysql://"+username+":"+password+"@localhost:3306/DatabaseETL"
engine = create_engine(path)
session = Session(engine)
if not database_exists(path):
    create_database(path)


Base = declarative_base()