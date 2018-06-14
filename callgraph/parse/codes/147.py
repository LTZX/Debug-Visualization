    def setUp(self):
        super(TestGroup, self).setUp()

        self.course = Course(offering='cal/cs61a/sp16')
        self.assignment = Assignment(
            name='cal/cs61a/sp16/proj1',
            course=self.course,
            display_name='Hog',
            due_date=datetime.datetime.now(),
            lock_date=datetime.datetime.now() + datetime.timedelta(days=1),
            max_group_size=4)
        db.session.add(self.assignment)

