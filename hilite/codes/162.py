    def test_remove_self(self):
        Group.invite(self.user1, self.user2, self.assignment)
        Group.invite(self.user1, self.user3, self.assignment)
        group = Group.lookup(self.user1, self.assignment)
        group.accept(self.user2)
        group.accept(self.user3)
        group.remove(self.user1, self.user1)

        assert Group.lookup(self.user1, self.assignment) is None
        assert group.has_status(self.user2, 'active')
        assert group.has_status(self.user3, 'active')

