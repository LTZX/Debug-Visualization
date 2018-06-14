    def test_decline_degenerate(self):
        Group.invite(self.user1, self.user2, self.assignment)
        group = Group.lookup(self.user1, self.assignment)
        group.decline(self.user2)

        assert Group.lookup(self.user1, self.assignment) is None
        assert Group.lookup(self.user2, self.assignment) is None

