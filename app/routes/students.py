from flask import (
    Blueprint,
    render_template,
)
from ..controllers.library_controller import lists


students_scope = Blueprint('students_scope', __name__)


@students_scope.route('/', methods=['GET'])
def home():
    return render_template('students/home.html')


@students_scope.route('/library', methods=['GET'])
def library():
    data = lists()
    return render_template('students/library.html', data=data)



