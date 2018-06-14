class BackupSchema(APISchema):

    get_fields = {
        'id': fields.Integer,
        'submitter': fields.Integer,
        'assignment': fields.Integer,
        'messages': fields.List(fields.Nested(MessageSchema.get_fields)),
        'client_time': fields.DateTime(dt_format='rfc822'),
        'created': fields.DateTime(dt_format='rfc822')
    }

    post_fields = {
        'id': fields.Integer,
        'url': fields.String,
        'message': fields.String,
    }

