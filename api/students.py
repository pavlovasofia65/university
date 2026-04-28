from flask import Blueprint, render_template
from models import Student

students_bp = Blueprint('students', __name__)

@students_bp.route('/students')
def list_students():
    return render_template('students/students.html')