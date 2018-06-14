    def validate(self):
        check_validate = super(AssignmentForm, self).validate()

        # if our validators do not pass
        if not check_validate:
            return False

        # Ensure assignment offering is unique
        assgn = Assignment.query.filter_by(name=self.name.data).first()
        if assgn:
            self.name.errors.append('That offering already exists')
            return False
        return True


