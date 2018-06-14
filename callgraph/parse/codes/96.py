class Message(db.Model, TimestampMixin):
    id = db.Column(db.Integer(), primary_key=True)
    backup = db.Column(db.ForeignKey("backup.id"), index=True)
    contents = db.Column(pg.JSONB())
    kind = db.Column(db.String(), index=True)

