@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)

