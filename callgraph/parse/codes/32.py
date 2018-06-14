class SubmissionSchema(BackupSchema):

    get_fields = {
        'id': fields.Integer,
        'assignment': fields.Integer,
        'submitter': fields.Integer,
        'backup': fields.Nested(BackupSchema.get_fields),
        'flagged': fields.Boolean,
        'revision': fields.Boolean,
        'created': fields.DateTime(dt_format='rfc822')
    }

