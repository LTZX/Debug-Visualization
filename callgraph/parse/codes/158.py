    def test_locked(self):
        Group.invite(self.user1, self.user2, self.assignment)
        Group.invite(self.user1, self.user3, self.assignment)
        Group.invite(self.user1, self.user4, self.assignment)
        group = Group.lookup(self.user1, self.assignment)
        group.accept(self.user2)

        self.assignment.lock_date = datetime.datetime.now() - datetime.timedelta(days=1)
        db.session.commit()

        self.assertRaises(BadRequest, Group.invite, self.user1, self.user2, self.assignment)
        self.assertRaises(BadRequest, group.accept, self.user3)
        self.assertRaises(BadRequest, group.decline, self.user3)
        self.assertRaises(BadRequest, group.remove, self.user1, self.user2)

