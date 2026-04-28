from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from api.courses import courses_bp
from api.disciplines import disciplines_bp
from api.groups import groups_bp
from api.students import students_bp
from api.teachers import teachers_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:Kikorik9!@localhost:14330/university?driver=ODBC+Driver+17+for+SQL+Server'
db = SQLAlchemy()

app.register_blueprint(courses_bp)
app.register_blueprint(disciplines_bp)
app.register_blueprint(groups_bp)
app.register_blueprint(students_bp)
app.register_blueprint(teachers_bp)

@app.route('/')
def main_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)