class TimestampMixin(object):
    created = db.Column(db.DateTime, server_default=db.func.now())


