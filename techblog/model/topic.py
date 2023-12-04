from flask import Flask
from dataclasses import dataclass
from sqlalchemy import Column, Integer, Date
from sqlalchemy.dialects.mysql import LONGTEXT
from base import Base
app = Flask(__name__)

@dataclass
class Topic(Base):
    __tablename__ = 'topic'

    topic_id = Column(Integer, primary_key=True)
    name = Column(LONGTEXT)

    def __init__(self, topic_id, name):
        self.topic_id = topic_id
        self.name = name

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}