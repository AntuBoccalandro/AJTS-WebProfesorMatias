from flask import (
    Blueprint,
    render_template,
)

errors_scope = Blueprint("errors_scope", __name__)

@errors_scope.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/error_template.html', code=404, error=error), 404


@errors_scope.app_errorhandler(500)
def internal_server_error(error):
    return render_template('errors/error_template.html', code=500, error=error), 500






