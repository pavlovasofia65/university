from flask import Blueprint, render_template, request, redirect, url_for
from models import Student, Group
from extensions import db

students_bp = Blueprint('students', __name__)

@students_bp.route('/students')
def list_students():
    query = db.select(Student).order_by(Student.group_id)
    students = db.session.execute(query).scalars().all()
    return render_template('students/students.html', students=students)

@students_bp.route('/students/<int:id>')
def student_detail(id):
    student = db.get_or_404(Student, id)
    return render_template('students/student.html', student=student)

@students_bp.route('/students/add', methods=['GET', 'POST'])
def add_student():
    groups = db.session.execute(db.select(Group)).scalars().all()
    if request.method == 'POST':
        try:
            new_student = Student(
                name = request.form['name'],
                surname = request.form['surname'],
                middle_name = request.form['middle_name'],
                group_id = request.form['group_id']
                )
            db.session.add(new_student)
            db.session.commit()
            return redirect(url_for('students.list_students'))
        except Exception as e:
            db.session.rollback()
            return f"Error: {str(e)}"
    return render_template('students/student_form.html', groups=groups)

@students_bp.route('/students/edit/<int:id>', methods = ['GET', 'POST'])
def edit_student(id):
    student = db.get_or_404(Student, id)
    groups = db.session.execute(db.select(Group)).scalars().all()
    if request.method == 'POST':
        try:
            student.name = request.form['name']
            student.surname = request.form['surname'],
            student.middle_name = request.form['middle_name'],
            student.group_id = request.form['group_id']

            db.session.commit()
            return redirect(url_for('students/student_detail', id=id))
        except Exception as e:
            db.session.rollback()
            return f"Error: {str(e)}"
    return render_template('students/student_form.html', student=student, groups=groups, is_edit=True)

@students_bp.route('/students/delete/<int:id>', methods=['GET', 'POST'])
def delete_student(id):
    student = db.get_or_404(Student, id)
    print(student)
    try:
        db.session.delete(student)
        db.session.commit()
        return redirect('/students')
    except Exception as e:
        db.session.rollback()
        return f"Помилка при видаленні: {str(e)}", 500