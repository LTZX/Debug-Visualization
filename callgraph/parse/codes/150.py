    def test_decline(self):
        Group.invite(self.user1, self.user2, self.assignment)
        Group.invite(self.user1, self.user3, self.assignment)
        group = Group.lookup(self.user1, self.assignment)
        group.accept(self.user2)
        group.decline(self.user3)

        assert group.has_status(self.user1, 'active')
        assert group.has_status(self.user2, 'active')
        assert Group.lookup(self.user3, self.assignment) is None
        assert group.size() == 2

