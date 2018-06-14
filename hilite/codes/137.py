    def tearDown(self):
        db.session.remove()
        db.drop_all()

