from flask import Blueprint, render_template
from models import Course

teachers_bp = Blueprint('teachers', __name__)

@teachers_bp.route('/teachers')
def list_teachers():
    return render_template('teachers/teachers.html')