from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root%40123@localhost/university"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def home():
    if request.method =='POST' and 'umich_id' in request.form:
        umid_entered = request.form['umich_id']

        if umid_entered:
            try:
                query = text("SELECT * FROM students WHERE umich_id = :umid")
                result = db.session.execute(query, {'umid': umid_entered}).fetchone()

                if result:

                    return render_template('page2.html')

                else:
                    return "Not a UMICH student"
            except Exception as e:
                return f"Error: {str(e)}"
        else:
            return "UMID not provided"

    return render_template('login.html')


# @app.route('/department')

if __name__ == '__main__':
    app.run(debug=True)



