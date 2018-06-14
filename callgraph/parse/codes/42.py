    @marshal_with(schema.get_fields)
    def get(self, user, key=None):
        if key is None:
            restful.abort(405)
        backup = self.model.query.filter_by(id=key).first()
        # TODO CHECK
        if backup.user != user or not user.is_admin:
            restful.abort(403)

        return backup

