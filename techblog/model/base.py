from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
app = Flask(__name__)
connection_string = "mysql+mysqlconnector://root:abc123ABC@localhost:3306/techblog"
engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)

Base = declarative_base()