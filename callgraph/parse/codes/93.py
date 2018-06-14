class GradingTask(db.Model, TimestampMixin):
    """Each task represent a single submission assigned to a grader."""
    id = db.Column(db.Integer(), primary_key=True)
    assignment = db.Column(db.ForeignKey("assignment.id"), index=True,
                           nullable=False)
    backup = db.Column(db.ForeignKey("backup.id"), nullable=False)
    course = db.Column(db.ForeignKey("course.id"))
    primary_owner = db.Column(db.ForeignKey("user.id"), index=True)
    kind = db.Column(db.Text())  # e.g. "composition"
    description = db.Column(db.Text())  # e.g. "Helpful links for grading"

