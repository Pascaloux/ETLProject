from sqlalchemy import *
from sqlalchemy_utils import *
from sqlalchemy.orm import *

username = input("username : ")
password = input("password : ")

url="mysql://"+username+":"+password+"@localhost:3306/test"
engine = create_engine(url)

if not database_exists(url):
    create_database(url)
    

Base = declarative_base()