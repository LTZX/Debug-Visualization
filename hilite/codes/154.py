    def test_invite_full(self):
        Group.invite(self.user1, self.user2, self.assignment)
        Group.invite(self.user1, self.user3, self.assignment)
        Group.invite(self.user1, self.user4, self.assignment)
        group = Group.lookup(self.user1, self.assignment)
        group.accept(self.user2)

        assert group.size() == 4
        self.assertRaises(BadRequest, Group.invite, self.user1, self.user5, self.assignment)

