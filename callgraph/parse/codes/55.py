def authorize_user(user):
    login_user(user)
    flash("Logged in successfully.", "success")
    after_login = session.pop('after_login', None)
    return redirect(after_login or url_for("main.home"))

