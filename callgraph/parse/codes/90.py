class CommentBank(db.Model, TimestampMixin):
    """ CommentBank is a set of common comments for assignments.
    An assignment value of null applies to all assignments.
    The statistics column will be used by the frontend.
    """
    id = db.Column(db.Integer(), primary_key=True)
    assignment = db.Column(db.ForeignKey("assignment.id"), index=True)
    author = db.Column(db.ForeignKey("user.id"), nullable=False)
    message = db.Column(db.Text())  # Markdown
    frequency = db.Column(db.Integer())
    statistics = db.Column(pg.JSONB())  # closest function, line number etc


