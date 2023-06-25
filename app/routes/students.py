from flask import (
    Blueprint,
    render_template,
)
from ..controllers.library_controller import lists
from app import cache


students_scope = Blueprint('students_scope', __name__)


@students_scope.route('/', methods=['GET'])
@cache.cached()
def home():
    return render_template('students/home.html')


@students_scope.route('/library', methods=['GET'])
@cache.cached()
def library():
    data = lists()
    return render_template('students/library.html', data=data)



