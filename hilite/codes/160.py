    def test_remove_degenerate(self):
        Group.invite(self.user1, self.user2, self.assignment)
        group = Group.lookup(self.user1, self.assignment)
        group.remove(self.user1, self.user1)

        assert Group.lookup(self.user1, self.assignment) is None
        assert Group.lookup(self.user2, self.assignment) is None

