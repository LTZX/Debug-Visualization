@admin.route("/course/<int:cid>/enrollment",
             methods=['GET', 'POST'], defaults={'page': 1})
@admin.route("/course/<int:cid>/enrollment/page/<int:page>",)
@is_staff(course_arg='cid')
def enrollment(cid, page):
    courses, current_course = get_courses(cid)
    single_form = forms.EnrollmentForm(prefix="single")
    if single_form.validate_on_submit():
        email, role = single_form.email.data, single_form.role.data
        Participant.enroll_from_form(cid, single_form)
        flash("Added {email} as {role}".format(email=email, role=role), "success")

    query = request.args.get('query', '').strip()
    students = None
    if query:
        find_student = User.query.filter_by(email=query)
        student = find_student.first()
        if student:
            students = Participant.query.filter_by(course_id=cid, role=STUDENT_ROLE,
                user_id=student.id).paginate(page=page, per_page=1)
        else:
            flash("No student found with email {}".format(query), "warning")
    if not students:
        students = Participant.query.filter_by(course_id=cid,
                role=STUDENT_ROLE).paginate(page=page, per_page=5)
    staff = Participant.query.filter(Participant.course_id == cid,
            Participant.role.in_(STAFF_ROLES)).all()

    return render_template('staff/course/enrollment.html',
                           enrollments=students, staff=staff, query=query,
                           single_form=single_form,
                           courses=courses,
                           current_course=current_course)


