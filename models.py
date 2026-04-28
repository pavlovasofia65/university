from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Major(db.Model):
    __tablename__ = 'Majors'
    id = db.Column(db.Integer, primary_key=True)

class Curriculum(db.Model):
    __tablename__ = 'Curriculums'
    id = db.Column(db.Integer, primary_key=True)

class Department(db.Model):
    __tablename__ = 'Departments'
    id = db.Column(db.Integer, primary_key=True)

class Teacher(db.Model):
    __tablename__ = 'Teachers'
    id = db.Column(db.Integer, primary_key=True)

class Group(db.Model):
    __tablename__ = 'Groups'
    id = db.Column(db.Integer, primary_key=True)

class Student(db.Model):
    __tablename__ = 'Students'
    id = db.Column(db.Integer, primary_key=True)

class Discipline(db.Model):
    __tablename__ = 'Disciplines'
    id = db.Column(db.Integer, primary_key=True)

class Lesson(db.Model):
    __tablename__ = 'Lessons'
    id = db.Column(db.Integer, primary_key=True)

class Teacher_WP(db.Model):
    __tablename__ = 'Teacher_work_plan'
    id = db.Column(db.Integer, primary_key=True)

class Lesson_Groups(db.Model):
    __tablename__ = 'Lesson_Groups'
    id = db.Column(db.Integer, primary_key=True)

class Curriculum_Details(db.Model):
    __tablename__ = 'Curriculum_Details'
    id = db.Column(db.Integer, primary_key=True)

class Course:
    __tablename__ = 'None'
    id = db.Column(db.Integer, primary_key=True)