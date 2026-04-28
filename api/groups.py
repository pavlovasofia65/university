from flask import Blueprint, render_template
from models import Course

groups_bp = Blueprint('groups', __name__)

@groups_bp.route('/groups')
def list_groups():
    return render_template('groups/groups.html')