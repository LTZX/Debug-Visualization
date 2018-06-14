@manager.command
def seed():
    """ Create default records for development.
    """
    staff_member = User(email='okstaff@okpy.org')
    db.session.add(staff_member)
    courses = [Course(offering="cs61a/test16", display_name="CS61A (Test)"),
               Course(offering="ds8/test16", display_name="DS8 (Test)")]
    db.session.add_all(courses)
    future = datetime.now() + timedelta(days=1)
    db.session.commit()

    students = [User(email='student{}@okpy.org'.format(i)) for i in range(60)]
    db.session.add_all(students)

    assign = Assignment(name="cs61a/sp16/test", creator=staff_member.id,
                        course_id=courses[0].id, display_name="test",
                        due_date=future, lock_date=future)
    db.session.add(assign)
    db.session.commit()
    staff = Participant(user_id=staff_member.id, course_id=courses[0].id,
                        role="staff")
    db.session.add(staff)
    student_enrollment = [Participant(user_id=student.id, role="student",
                          course_id=courses[0].id) for student in students]
    db.session.add_all(student_enrollment)

    db.session.commit()


