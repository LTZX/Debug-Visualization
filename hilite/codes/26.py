class MessageSchema(APISchema):
    """ Messages do not have their own API (currently).
    They are displayed through the backup/submission APIs.
    """
    get_fields = {
        'kind': fields.String,
        'contents': fields.String,
        'created': fields.DateTime(dt_format='rfc822')
    }


