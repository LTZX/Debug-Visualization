class ParticipationSchema(APISchema):
    get_fields = {
        'course_id': fields.Integer,
        'role': fields.String,
        'course': fields.Nested(CourseSchema.get_fields),
    }

