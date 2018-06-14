    @staticmethod
    def enroll_from_form(cid, form):
        usr = User.lookup(form.email.data)
        if usr:
            form.populate_obj(usr)
        else:
            usr = User()
            form.populate_obj(usr)
            db.session.add(usr)
        db.session.commit()
        role = form.role.data
        Participant.create(cid, [usr.id], role)

