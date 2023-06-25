from flask import (
    Blueprint,
    render_template,
    redirect,
    request
)
from ..controllers.admin_controller import (
    lists,
    insert,
    delete,
)
from ..helpers.filename_formater import format_filenames
from ..helpers.file_saver import save_files
from config.config import Config
from .login import login_required
from app import cache

admin_scope = Blueprint('admin_scope', __name__)


@admin_scope.route('/', methods=['GET'])
@login_required
@cache.cached()
def home():
    return render_template('admin/home.html')


@admin_scope.route('/admin_library', methods=['GET'])
@login_required
@cache.cached()
def library():  
    data = lists()
    return render_template('admin/library.html', data=data)


@admin_scope.route('/dashboard', methods=['GET'])
@login_required
@cache.cached()
def dashboard():
    data = lists()
    return render_template('admin/dashboard.html', data=data)


@admin_scope.route('/dashboard/actions/create', methods=['POST'])
@login_required
def create_book():
    requested_book_name = request.form['field_book_name']
    requested_book_file = request.files['field_book_file']
    requested_book_cover = request.files['field_book_cover']

    new_book_filename, new_book_covername = format_filenames(requested_book_file.filename, requested_book_cover.filename)

    save_files(
        [requested_book_file, Config.FILES_FOLDER+new_book_filename], 
        [requested_book_cover, Config.COVERS_FOLDER+new_book_covername]
        )
    
    insert(requested_book_name, new_book_filename, new_book_covername)

    return redirect('/admin/dashboard')


@admin_scope.route('/dashboard/actions/delete', methods=['POST'])
@login_required
def delete_book():
    book_name = request.form['book_name']
    book_filename = request.form['book_filename']
    book_covername = request.form['book_covername']

    delete(book_name, book_filename, book_covername)
    return redirect('/admin/dashboard')
