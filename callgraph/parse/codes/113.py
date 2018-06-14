    @transaction
    def decline(self, user):
        """Decline an invitation."""
        if not self.assignment.active:
            raise BadRequest('The assignment is past due')
        self._remove_member(user)

