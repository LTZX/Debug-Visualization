class APISchema():
    """ APISchema describes the input and output formats for
    resources. The parser deals with arguments to the API.
    The API responses are marshalled to json through get_fields
    """
    get_fields = {
        'id': fields.Integer,
        'created': fields.DateTime(dt_format='rfc822')
    }

