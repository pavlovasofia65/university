from flask import Blueprint, render_template
# from models import Course

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/courses')
def list_courses():
    return render_template('courses/courses.html')