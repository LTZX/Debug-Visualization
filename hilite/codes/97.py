class Participant(db.Model, TimestampMixin):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.ForeignKey("user.id"), index=True, nullable=False)
    course_id = db.Column(db.ForeignKey("course.id"), index=True,
                          nullable=False)
    role = db.Column(db.Enum(*VALID_ROLES, name='role'), default=STUDENT_ROLE, nullable=False)

    user = db.relationship("User", backref="participations")
    course = db.relationship("Course", backref="participants")
    notes = db.Column(db.String()) # For Section Info etc.

