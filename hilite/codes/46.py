    @marshal_with(schema.get_fields)
    def get(self, email):
        course = request.args.get('course', '')  # TODO use reqparse
        user = models.User.lookup(email)
        if course and user:
            return {'courses': user.participations}
        return {'courses': []}

api.add_resource(v3Info, '/v3')

api.add_resource(Submission, '/v3/submission', '/v3/submission/<int:key>')
api.add_resource(Backup, '/v3/backup', '/v3/backup/<int:key>')
api.add_resource(Score, '/v3/score')
