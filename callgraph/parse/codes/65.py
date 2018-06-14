@auth.route('/testing-login')
def testing_login():
    if not use_testing_login():
        abort(404)
    return render_template('testing-login.html', callback=url_for(".testing_authorized"))

