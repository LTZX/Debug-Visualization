    def test_accept_not_pending(self):
        Group.invite(self.user1, self.user2, self.assignment)
        group = Group.lookup(self.user1, self.assignment)
        group.accept(self.user2)

        self.assertRaises(BadRequest, group.accept, self.user2)
        self.assertRaises(BadRequest, group.accept, self.user3)

