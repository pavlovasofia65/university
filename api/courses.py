# Not sure to do this at all
from flask import Blueprint, render_template
from models import Course

courses_bp = Blueprint('courses', __name__)
Course = Course()

@courses_bp.route('/courses')
def list_courses():
    courses = Course.query.order_by()
    return render_template('courses/courses.html')

@courses_bp.route('/courses/<int:id>')
def course_details():
    return render_template('courses/course.html')

@courses_bp.route('/courses/create-course', methods=['POST', 'GET'])
def create_course():
    return render_template('/courses/create_course.html')

@courses_bp.route('/courses/delete')
def delete_course():
    return