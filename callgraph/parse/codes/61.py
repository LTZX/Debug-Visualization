@auth.route("/logout")
def logout():
    logout_user()
    session.pop('google_token', None)
    flash("You have been logged out.", "success")
    return redirect(url_for("main.home"))

