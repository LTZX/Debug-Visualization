        def make_student(n):
            user = User(email='student{0}@aol.com'.format(n))
            participant = Participant(
                user=user,
                course=self.course)
            db.session.add(participant)
            return user

        self.user1 = make_student(1)
        self.user2 = make_student(2)
        self.user3 = make_student(3)
        self.user4 = make_student(4)
        self.user5 = make_student(5)
        db.session.commit()

