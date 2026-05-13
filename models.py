from flask_sqlalchemy import SQLAlchemy
from extensions import db

class Major(db.Model):
    __tablename__ = 'Majors'
    id = db.Column('major_id', db.Integer, primary_key=True)
    name = db.Column('major_name', db.String(45), unique=True, nullable=False)

class Curriculum(db.Model):
    __tablename__ = 'Curriculums'
    id = db.Column('curriculum_id', db.Integer, primary_key=True)
    major_id = db.Column('curriculum_major', db.Integer, db.ForeignKey('Majors.major_id'), nullable=False)
    major = db.relationship('Major', backref=db.backref('curriculums', lazy=True))
    year = db.Column('curriculum_year', db.Date, nullable=False)

class Department(db.Model):
    __tablename__ = 'Departments'
    id = db.Column('dep_id', db.Integer, primary_key=True)
    name = db.Column('dep_name', db.String(45), unique=True, nullable=False)

class Teacher(db.Model):
    __tablename__ = 'Teachers'
    id = db.Column('teacher_id', db.Integer, primary_key=True)
    name = db.Column('teacher_name', db.String(45), nullable=False)
    surname = db.Column('teacher_surname', db.String(45), nullable=False)
    middle_name = db.Column('teacher_middle_name', db.String(45), nullable=False)
    department_id = db.Column('teacher_department', db.Integer, db.ForeignKey('Departments.dep_id'), nullable=False)
    department = db.relationship('Department', backref=db.backref('teachers', lazy=True))
    rate = db.Column('teacher_rate', db.String(45), nullable=False)
    email = db.Column('teacher_email', db.String(45), unique=True, nullable=False)

class Group(db.Model):
    __tablename__ = 'Groups'
    id = db.Column('group_id', db.Integer, primary_key=True)
    name = db.Column('group_name', db.String(45), nullable=False)
    course = db.Column('group_course', db.Integer, nullable=False)
    major_id = db.Column('group_major', db.Integer, db.ForeignKey('Majors.major_id'), nullable=False)
    major = db.relationship('Major', backref=db.backref('groups', lazy=True))
    advisor_id = db.Column('group_advisor', db.Integer, db.ForeignKey('Teachers.teacher_id'), nullable=False)
    advisor = db.relationship('Teacher', backref=db.backref('teachers', lazy=True))
    curriculum_id = db.Column('group_curriculum', db.Integer, db.ForeignKey('Curriculums.curriculum_id'), nullable=False)
    curriculum = db.relationship('Curriculum', backref=db.backref('groups', lazy=True))

class Student(db.Model):
    __tablename__ = 'Students'
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column('student_name', db.String(45), nullable=False)
    surname = db.Column('student_surname', db.String(45), nullable=False)
    middle_name = db.Column('student_middle_name', db.String(45), nullable=False)
    group_id = db.Column('student_group', db.Integer, db.ForeignKey('Groups.group_id'), nullable=False)
    group = db.relationship('Group', backref=db.backref('students', lazy=True))

class Discipline(db.Model):
    __tablename__ = 'Disciplines'
    id = db.Column('discipline_id', db.Integer, primary_key=True)
    name = db.Column('discipline_name', db.String(45), nullable=False)
    control = db.Column('discipline_control', db.String(45), nullable=False)
    hours = db.Column('discipline_hours', db.Integer, nullable=False)

class Lesson(db.Model):
    __tablename__ = 'Lessons'
    id = db.Column('lesson_id', db.Integer, primary_key=True)
    discipline_id = db.Column('lesson_discipline', db.Integer, db.ForeignKey('Disciplines.discipline_id'), nullable=False)
    discipline = db.relationship('Discipline', backref=db.backref('lessons', lazy=True))
    teacher_id = db.Column('lesson_teacher', db.Integer, db.ForeignKey('Teachers.teacher_id'), nullable=False)
    teacher = db.relationship('Teacher', backref=db.backref('lessons', lazy=True))
    date = db.Column('lesson_day', db.Date, nullable=False)
    time = db.Column('lesson_time', db.Time, nullable=False)
    type = db.Column('lesson_type', db.String(45), nullable=False)
    location = db.Column('lesson_location', db.String(45), nullable=False)

class Lesson_Groups(db.Model):
    __tablename__ = 'Lesson_Groups'
    lesson_id = db.Column('lg_lesson_id', db.Integer, db.ForeignKey('Lessons.lesson_id'), primary_key=True)
    lesson = db.relationship('Lesson', backref=db.backref('lessons_groups', lazy=True))
    group_id = db.Column('lg_group_id', db.Integer, db.ForeignKey('Groups.group_id'), primary_key=True)
    group = db.relationship('Group', backref=db.backref('lessons_groups', lazy=True))

class Teacher_WP(db.Model):
    __tablename__ = 'Teacher_work_plan'
    id = db.Column('tw_id', db.Integer, primary_key=True)
    teacher_id = db.Column('tw_teacher', db.Integer, db.ForeignKey('Teachers.teacher_id'), nullable=False)
    teacher = db.relationship('Teacher', backref=db.backref('teacher_wp', lazy=True))
    hours = db.Column('tw_hours', db.Integer, nullable=False)
    speciality = db.Column('tw_speciality', db.String(45), nullable=False)

class Curriculum_Details(db.Model):
    __tablename__ = 'Curriculum_Details'
    id = db.Column('cd_id', db.Integer, primary_key=True)
    curriculum_id = db.Column('cd_curriculum_id', db.Integer, db.ForeignKey('Curriculums.curriculum_id'), nullable=False)
    curriculum = db.relationship('Curriculum', backref=db.backref('curriculum_details', lazy=True))
    discipline_id = db.Column('cd_discipline_id', db.Integer, db.ForeignKey('Disciplines.discipline_id'), nullable=False)
    discipline = db.relationship('Discipline', backref=db.backref('curriculum_details', lazy=True))
    semester = db.Column('cd_semester', db.Integer, nullable=False)
    lectures_hours = db.Column('cd_lectures_hours', db.Integer, nullable=False)
    practice_hours = db.Column('cd_practice_hours', db.Integer, nullable=False)
    control_type = db.Column('cd_control_type', db.String(45))