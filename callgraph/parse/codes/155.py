    def test_invite_in_group(self):
        Group.invite(self.user1, self.user2, self.assignment)

        self.assertRaises(BadRequest, Group.invite, self.user1, self.user1, self.assignment)
        self.assertRaises(BadRequest, Group.invite, self.user1, self.user2, self.assignment)

        self.assertRaises(BadRequest, Group.invite, self.user2, self.user1, self.assignment)
        self.assertRaises(BadRequest, Group.invite, self.user2, self.user2, self.assignment)
        self.assertRaises(BadRequest, Group.invite, self.user2, self.user3, self.assignment)

        self.assertRaises(BadRequest, Group.invite, self.user3, self.user1, self.assignment)
        self.assertRaises(BadRequest, Group.invite, self.user3, self.user2, self.assignment)
        self.assertRaises(BadRequest, Group.invite, self.user3, self.user3, self.assignment)

