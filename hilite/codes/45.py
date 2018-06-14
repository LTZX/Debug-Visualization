    def store_backup(self, user):
        args = self.parse_args()
        # TODO Assignment Memcache.
        assignment = models.Assignment.query.filter_by(
            name=args['assignment']).first()
        messages, submit, submitter = args['messages'], args['submit'], user
        backup = make_backup(user, assignment, messages, submit, submitter)
        return backup


