class Group(db.Model, TimestampMixin):
    """A group is a collection of users who are either members or invited.
    Groups are created when a member not in a group invites another member.
    Invited members may accept or decline invitations. Active members may
    revoke invitations and remove members (including themselves).
    A group must have at least 2 participants.
    Degenerate groups are deleted.
    """
    id = db.Column(db.Integer(), primary_key=True)
    assignment_id = db.Column(db.ForeignKey("assignment.id"), nullable=False)

    assignment = db.relationship("Assignment")

