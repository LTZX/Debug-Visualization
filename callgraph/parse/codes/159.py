    def test_remove(self):
        Group.invite(self.user1, self.user2, self.assignment)
        Group.invite(self.user1, self.user3, self.assignment)
        Group.invite(self.user1, self.user4, self.assignment)
        group = Group.lookup(self.user1, self.assignment)
        group.accept(self.user2)

        group.remove(self.user1, self.user2)
        assert group.has_status(self.user1, 'active')
        assert Group.lookup(self.user2, self.assignment) is None
        assert group.has_status(self.user3, 'pending')
        assert group.size() == 3

        group.remove(self.user1, self.user3)
        assert group.has_status(self.user1, 'active')
        assert Group.lookup(self.user3, self.assignment) is None
        assert group.size() == 2

