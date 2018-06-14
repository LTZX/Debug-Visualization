    def test_remove_not_in_group(self):
        Group.invite(self.user1, self.user2, self.assignment)
        group = Group.lookup(self.user1, self.assignment)
        group.accept(self.user2)

        self.assertRaises(BadRequest, group.remove, self.user2, self.user3)
