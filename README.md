## Project Title/Name: Tech_Blog

Description:

* Developing a comprehensive platform that allows students and professors to create and share articles related to tech, projects, and academic research. 
* Utilizing a database to store and manage user-generated content and implemented AI-driven features to enhance user experience and content discoverability. Employing web development technologies and frameworks to create an intuitive and interactive user interface.
* Facilitated collaboration and knowledge sharing within the University of Michigan academic community.


Prerequisites:
python,
MySQL,
MySQL workbench.

Tools that need to be installed before running the project.
Python (version 3.x)
Flask
Flask-SQLAlchemy
MySQL or another compatible database
Git

Installation:


# Clone the repository
git clone https://github.com/Rakshasv18/Tech_Blog.git

# Navigate to the project directory
cd your-repo

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'

# Install dependencies
pip install -r requirements.txt


Database Setup:

Provide instructions on how to set up the database.
bash
Copy code
# Create a MySQL database named 'university'
# Update the 'SQLALCHEMY_DATABASE_URI' in your Flask app accordingly

# Run the following commands in your MySQL shell or a database management tool
CREATE DATABASE university;

# Optionally, create a MySQL user and grant privileges
CREATE USER 'your-username'@'localhost' IDENTIFIED BY 'your-password';
GRANT ALL PRIVILEGES ON university.* TO 'your-username'@'localhost';

# Run the Flask app
python app.py

Open your web browser and go to http://127.0.0.1:5000/ in the address bar.


Contributers:
1.Surya 
2.Jayani
3.Pallavi
4.Raksha 
