from flask import Blueprint, render_template
from models import Discipline

disciplines_bp = Blueprint('disciplines', __name__)

@disciplines_bp.route('/disciplines')
def list_disciplines():
    return render_template('disciplines/disciplines.html')

@disciplines_bp.route('/disciplines/<int:id>')
def discipline_details():
    return render_template('disciplines/discipline')