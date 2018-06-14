    @staticmethod
    def enroll_from_csv(cid, form):
        new_users, existing_uids = [], []
        rows = form.csv.data.splitlines()
        entries = list(csv.reader(rows))
        for usr in entries:
            email, name, sid, login, notes = usr
            usr_obj = User.lookup(email)
            if not usr_obj:
                usr_obj = User(email=email, name=name, sid=sid, secondary=login)
                new_users.append(usr_obj)
            else:
                usr_obj.name = name
                usr_obj.sid = sid
                usr_obj.secondary = login
                usr_obj.notes = notes
                existing_uids.append(usr_obj.id)

        db.session.add_all(new_users)
        db.session.commit()
        user_ids = [u.id for u in new_users] + existing_uids
        Participant.create(cid, user_ids, STUDENT_ROLE)
        return len(new_users), len(existing_uids)


