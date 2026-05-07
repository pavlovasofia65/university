from flask import Blueprint, render_template
from models import Discipline
from extensions import db

disciplines_bp = Blueprint('disciplines', __name__)

@disciplines_bp.route('/disciplines')
def list_disciplines():
    return render_template('disciplines/disciplines.html')