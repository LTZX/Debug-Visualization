class Backup(db.Model, TimestampMixin):
    id = db.Column(db.Integer(), primary_key=True)
    messages = db.relationship("Message")
    scores = db.relationship("Score")
    client_time = db.Column(db.DateTime())
    submitter = db.Column(db.ForeignKey("user.id"), nullable=False)
    assignment = db.Column(db.ForeignKey("assignment.id"), nullable=False)
    submit = db.Column(db.Boolean(), default=False)
    flagged = db.Column(db.Boolean(), default=False)

    db.Index('idx_usrBackups', 'assignment', 'submitter', 'submit', 'flagged')
    db.Index('idx_usrFlagged', 'assignment', 'submitter', 'flagged')
    db.Index('idx_submittedBacks', 'assignment', 'submit')
    db.Index('idx_flaggedBacks', 'assignment', 'flagged')

