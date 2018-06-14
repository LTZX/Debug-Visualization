def user_from_email(email):
    """Get a User with the given email, or create one."""
    user = User.lookup(email)
    if not user:
        user = User(email=email)
        db.session.add(user)
        db.session.commit()
    return user

