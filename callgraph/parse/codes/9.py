@admin.route("/course/<int:cid>/enrollment/batch",
             methods=['GET', 'POST'])
@is_staff(course_arg='cid')
def batch_enroll(cid):
    courses, current_course = get_courses(cid)
    batch_form = forms.BatchEnrollmentForm()
    if batch_form.validate_on_submit():
        new, updated = Participant.enroll_from_csv(cid, batch_form)
        msg = "Added {new}, Updated {old} students".format(new=new, old=updated)
        flash(msg, "success")
        return redirect(url_for(".enrollment", cid=cid))

    return render_template('staff/course/enrollment.batch.html',
                           batch_form=batch_form,
                           courses=courses,
