@admin.route("/course/<int:cid>/assignments/new", methods=["GET", "POST"])
@is_staff(course_arg='cid')
def new_assignment(cid):
    courses, current_course = get_courses(cid)
    # TODO  Form Creation
    form = forms.AssignmentForm()

    if form.validate_on_submit():
        model = Assignment(course_id=cid, creator=current_user.id)
        form.populate_obj(model)
        # TODO CONVERT TO UTC from PST.
        db.session.add(model)
        db.session.commit()

        flash("Assignment created successfully.", "success")
        return redirect(url_for(".course_assignments", cid=cid))

    return render_template('staff/course/assignment.new.html', form=form,
                           courses=courses, current_course=current_course)


