    @staticmethod
    @transaction
    def invite(sender, recipient, assignment):
        """Invite a user to a group, creating a group if necessary."""
        if not assignment.active:
            raise BadRequest('The assignment is past due')
        group = Group.lookup(sender, assignment)
        if not group:
            group = Group(assignment=assignment)
            db.session.add(group)
            group._add_member(sender, 'active')
        elif not group.has_status(sender, 'active'):
            raise BadRequest('You are not in the group')
        group._add_member(recipient, 'pending')

