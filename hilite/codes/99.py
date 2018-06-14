class Submission(db.Model, TimestampMixin):
    """ A submission is created from --submit or when a backup is flagged for
    grading.

    **This model may be removed. Do not depend on it for features.**
    """
    id = db.Column(db.Integer(), primary_key=True)
    backup = db.Column(db.ForeignKey("backup.id"), nullable=False)
    assignment = db.Column(db.ForeignKey("assignment.id"), nullable=False)
    submitter = db.Column(db.ForeignKey("user.id"), nullable=False)
    flagged = db.Column(db.Boolean(), default=False)

    db.Index('idx_flaggedSubms', 'assignment', 'submitter', 'flagged'),


