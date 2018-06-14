    @staticmethod
    def create(cid, usr_ids=[], role=STUDENT_ROLE):
        new_records = []
        for usr_id in usr_ids:
            record = Participant.query.filter_by(user_id=usr_id,
                                                   course_id=cid).one_or_none()
            if record:
                record.role = role
            else:
                record = Participant(course_id=cid, user_id=usr_id, role=role)
                new_records.append(record)
        db.session.add_all(new_records)
        db.session.commit()


