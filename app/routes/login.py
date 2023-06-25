from flask import (
    Blueprint,
    render_template,
    redirect,
    request,
    session,
)


login_scope = Blueprint('login_scope', __name__)


def login_required():
    if 'user' not in session:
        return redirect('/login')


@login_scope.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['txtUser']
        password = request.form['txtPassword']
        if user == 'MatiasEzequiel' and password == 'Julio15':
            session['login'] = True
            session['user'] = 'Matías Ezequiel Cervi'
            return render_template('admin/home.html')
        else:
            return render_template('login/login.html', message=True)



    return render_template('login/login.html')


@login_scope.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect('/')


