class EnrollmentSchema(APISchema):

    get_fields = {
        'courses': fields.List(fields.Nested(ParticipationSchema.get_fields))
    }


