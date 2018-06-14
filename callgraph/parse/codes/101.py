class User(db.Model, UserMixin, TimestampMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String(), unique=True, nullable=False, index=True)
    is_admin = db.Column(db.Boolean(), default=False)
    sid = db.Column(db.String())  # SID or Login
    secondary = db.Column(db.String())  # Other usernames
    alt_email = db.Column(db.String())
    active = db.Column(db.Boolean(), default=True)

