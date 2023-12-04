from flask import Flask, json, jsonify, Response
import base
from students import Student
from topic import Topic
from article import Article

app = Flask(__name__)

@app.route('/students')
def list_students():
    session = base.Session()
    students = session.query(Student).all()
    return Response(json.dumps([ob.as_dict() for ob in students]),  mimetype='application/json')

@app.route('/students/<id>')
def list_student(id):
    session = base.Session()
    student = session.query(Student).filter(Student.umich_id == id).first()
    return student.as_dict()

@app.route('/topics')
def list_topics():
    session = base.Session()
    topics = session.query(Topic).all()
    return Response(json.dumps([ob.as_dict() for ob in topics]),  mimetype='application/json')

@app.route('/topics/<id>')
def list_topic(id):
    session = base.Session()
    topic = session.query(Topic).filter(Topic.topic_id == id).first()
    return topic.as_dict()

@app.route('/articles')
def list_articles():
    session = base.Session()
    articles = session.query(Article).all()
    return Response(json.dumps([ob.as_dict() for ob in articles]),  mimetype='application/json')

@app.route('/articles/<id>')
def list_article(id):
    session = base.Session()
    article = session.query(Article).filter(Article.article_id == id).first()
    return article.as_dict()

@app.route('/welcome')
def welcome():
    return 'Welcome'