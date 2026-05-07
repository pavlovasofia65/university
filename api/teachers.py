from flask import Blueprint, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import Teacher, Major, Department
from extensions import db

teachers_bp = Blueprint('teachers', __name__)

@teachers_bp.route('/teachers')
def list_teachers():
    query = db.select(Teacher).order_by(Teacher.surname)
    teachers = db.session.execute(query).scalars().all()
    return render_template('teachers/teachers.html', teachers=teachers)

@teachers_bp.route('/teachers/<int:id>')
def teacher_detail(id):
    teacher = db.get_or_404(Teacher, id)
    return render_template('teachers/teacher.html', teacher=teacher)

@teachers_bp.route('/teachers/add', methods=['GET', 'POST'])
def add_teacher():
    departments = db.session.execute(db.select(Department)).scalars().all()
    if request.method == 'POST':
        try:
            new_teacher = Teacher(
                name=request.form['name'],
                surname=request.form['surname'],
                middle_name=request.form.get('middle_name'),
                department_id=request.form['department_id'],
                rate=request.form['rate'],
                email=request.form['email']
            )
            db.session.add(new_teacher)
            db.session.commit()
            return redirect(url_for('teachers.list_teachers'))
        except Exception as e:
            db.session.rollback()
            return f"Error: {str(e)}"
    return render_template('teachers/teacher_form.html', departments=departments)

@teachers_bp.route('/teachers/edit/<int:id>', methods=['GET', 'POST'])
def edit_teacher(id):
    teacher = db.get_or_404(Teacher, id)
    departments = db.session.execute(db.select(Department)).scalars().all()

    if request.method == 'POST':
        try:
            teacher.name = request.form['name']
            teacher.surname = request.form['surname']
            teacher.middle_name = request.form.get('middle_name', '')
            teacher.department_id = request.form['department_id']
            teacher.rate = request.form['rate']
            teacher.email = request.form['email']
            
            db.session.commit()
            return redirect(url_for('teachers.teacher_detail', id=id))
        except Exception as e:
            db.session.rollback()
            return f"Error: {str(e)}"
            
    return render_template('teachers/teacher_form.html', teacher=teacher, departments=departments, is_edit=True)

@teachers_bp.route('/teachers/delete/<int:id>', methods=['GET', 'POST'])
def delete_teacher(id):
    teacher = db.get_or_404(Teacher, id)
    try:
        db.session.delete(teacher)
        db.session.commit()
        return redirect('/teachers')
    except Exception as e:
        db.session.rollback()
        return f"Помилка при видаленні: {str(e)}", 500