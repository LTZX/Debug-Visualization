    def test_invite_not_enrolled(self):
        not_enrolled = User(email='not_enrolled@aol.com')
        db.session.add(not_enrolled)

        self.assertRaises(BadRequest, Group.invite, self.user1, not_enrolled, self.assignment)
        self.assertRaises(BadRequest, Group.invite, not_enrolled, self.user1, self.assignment)

