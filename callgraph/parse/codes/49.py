    def post(self, user):
        # TODO : Actual arg parse here (for autograder)
        score = models.Score(backup=1, score=1,
                             tag="test", grader=user.id)
        models.db.session.add(score)
        models.db.session.commit()

        return {'id': score.id, 'backup': 1}


