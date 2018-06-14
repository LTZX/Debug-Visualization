class Course(db.Model, TimestampMixin):
    id = db.Column(db.Integer(), primary_key=True)
    offering = db.Column(db.String(), unique=True)
    # offering - E.g., 'cal/cs61a/fa14
    institution = db.Column(db.String())  # E.g., 'UC Berkeley'
    display_name = db.Column(db.String())
    creator = db.Column(db.ForeignKey("user.id"))
    active = db.Column(db.Boolean(), default=True)

