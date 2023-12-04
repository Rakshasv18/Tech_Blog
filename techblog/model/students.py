from flask import Flask
from dataclasses import dataclass
from sqlalchemy import Column, Integer, Date
from sqlalchemy.dialects.mysql import LONGTEXT
from base import Base
app = Flask(__name__)

@dataclass
class Student(Base):
    __tablename__ = 'students'

    umich_id = Column(Integer, primary_key=True)
    first_name = Column(LONGTEXT)
    last_name = Column(LONGTEXT)
    major = Column(LONGTEXT)

    def __init__(self, umich_id, first_name, last_name, major):
        self.umich_id = umich_id
        self.first_name = first_name
        self.last_name = last_name
        self.major = major

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}