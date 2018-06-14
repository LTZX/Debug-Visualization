    def test_decline_not_pending(self):
        Group.invite(self.user1, self.user2, self.assignment)
        group = Group.lookup(self.user1, self.assignment)

        self.assertRaises(BadRequest, group.decline, self.user3)

