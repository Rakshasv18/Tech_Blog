from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text 
from sqlalchemy import or_
from flask import jsonify

app = Flask(__name__)
app.secret_key = "hello"

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root%40123@localhost/university"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Homepage route
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def home():
    if request.method =='POST' and 'umich_id' in request.form:
        umid_entered = request.form['umich_id']

        if umid_entered:
            try:
                # SQL query to check if the entered UMID exists in the database
                query = text("SELECT * FROM students WHERE umich_id = :umid")
                result = db.session.execute(query, {'umid': umid_entered}).fetchone()

                if result:
                    # If UMID exists, render the search page
                    return render_template('Search_page_with_departments.html')
                else:
                    # If UMID doesn't exist, render the not umich student page
                    return render_template('Not_umich_student.html')
            except Exception as e:
                return f"Error: {str(e)}"
        else:
            # If no UMID entered, render the invalid UMID page
            return render_template("invalidUMID.html")

    return render_template('login.html')

# Select department route
@app.route('/select_department', methods=['GET', 'POST'])
def select_department():
    if request.method == 'POST' and 'department' in request.form:
        selected_department = request.form['department']
        # Store the selected_department in session or database for future reference
        return redirect(url_for('display_articles'))

    return render_template('Keyword search.html')

# Display articles route
@app.route('/display_articles', methods=['POST', 'GET'])
def display_articles():
    if request.method == 'POST' and 'keyword' in request.form:
        selected_keyword = request.form['keyword']

        # Using a raw SQL query to filter articles based on the keyword in the title
        query = text("SELECT * FROM articles WHERE title LIKE :keyword LIMIT 5")
        articles = db.session.execute(query, {'keyword': f'%{selected_keyword}%'}).fetchall()

        # Convert articles to a list of dictionaries
        articles_dict_list = [
            {'id': article[0], 'title': article[1], 'author': article[2], 'content': article[3]}
            for article in articles
        ]

        # Store articles in the session
        session['articles'] = articles_dict_list

    else:
        # If no keyword is provided, set an empty list for articles_dict_list
        articles_dict_list = []

    # Render the template with the articles_dict_list
    return render_template('Top_5_Corrected_Version copy.html', articles_dict_list=articles_dict_list)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
