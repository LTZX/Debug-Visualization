    def test_invite_individual(self):
        individual_assignment = Assignment(
            name='cal/cs61a/sp16/lab00',
            course=self.course,
            display_name='Lab 0',
            due_date=datetime.datetime.now(),
            lock_date=datetime.datetime.now() + datetime.timedelta(days=1),
            max_group_size=1)
        db.session.add(individual_assignment)

        self.assertRaises(BadRequest, Group.invite, self.user1, self.user2, individual_assignment)

