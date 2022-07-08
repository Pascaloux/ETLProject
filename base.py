from sqlalchemy import *
from sqlalchemy_utils import *
from sqlalchemy.orm import *

username = input("username : ")
password = input("password : ")

path="mysql://"+username+":"+password+"@localhost:3306/test"
engine = create_engine(path)

if not database_exists(path):
    create_database(path)
    

Base = declarative_base()