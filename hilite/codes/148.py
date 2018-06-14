    def test_accept(self):
        Group.invite(self.user1, self.user2, self.assignment)
        group = Group.lookup(self.user1, self.assignment)
        group.accept(self.user2)

        assert group.has_status(self.user1, 'active')
        assert group.has_status(self.user2, 'active')
        assert group.size() == 2

