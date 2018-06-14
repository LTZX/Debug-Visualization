    def test_invite(self):
        Group.invite(self.user1, self.user2, self.assignment)
        group = Group.lookup(self.user1, self.assignment)

        assert group.has_status(self.user1, 'active')
        assert group.has_status(self.user2, 'pending')
        assert group.size() == 2

        Group.invite(self.user1, self.user3, self.assignment)

        assert group.has_status(self.user1, 'active')
        assert group.has_status(self.user2, 'pending')
        assert group.has_status(self.user3, 'pending')
        assert group.size() == 3

