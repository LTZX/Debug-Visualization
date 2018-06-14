class CourseSchema(APISchema):
    get_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'display_name': fields.String,
        'active': fields.Boolean,
    }


