from flask import Flask
from dataclasses import dataclass
from sqlalchemy import Column, Integer, Date
from sqlalchemy.dialects.mysql import LONGTEXT
from base import Base
app = Flask(__name__)

@dataclass
class Article(Base):
    __tablename__ = 'articles'

    article_id = Column(Integer, primary_key=True)
    title = Column(LONGTEXT)
    author = Column(LONGTEXT)
    content = Column(LONGTEXT)

    def __init__(self, article_id, title, author, content):
        self.article_id = article_id
        self.title = title
        self.author = author
        self.content = content

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}