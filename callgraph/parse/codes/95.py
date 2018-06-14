class GroupMember(db.Model, TimestampMixin):
    """A member of a group must accept the invite to join the group.
    Only members of a group can view each other's submissions.
    A user may only be invited or participate in a single group per assignment.
    The status value can be one of:
        pending - The user has been invited to the group.
        active  - The user accepted the invite and is part of the group.
    """
    __tablename__ = 'GroupMember'
    __table_args__ = (
        PrimaryKeyConstraint('user_id', 'assignment_id', name='pk_GroupMember'),
    )
    status_values = ['pending', 'active']

    user_id = db.Column(db.ForeignKey("user.id"), nullable=False, index=True)
    assignment_id = db.Column(db.ForeignKey("assignment.id"), nullable=False)
    group_id = db.Column(db.ForeignKey("group.id"), nullable=False, index=True)

    status = db.Column(db.Enum(*status_values, name="status"), index=True)
    updated = db.Column(db.DateTime, onupdate=db.func.now())

    user = db.relationship("User")
    assignment = db.relationship("Assignment")
    group = db.relationship("Group",
        backref=backref('members', cascade="all, delete-orphan"))


