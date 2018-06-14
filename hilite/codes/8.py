@admin.route("/course/<int:cid>/assignments/<int:aid>",
             methods=['GET', 'POST'])
@is_staff(course_arg='cid')
def assignment(cid, aid):
    courses, current_course = get_courses(cid)
    assgn = Assignment.query.filter_by(id=aid, course_id=cid).one()
    # Convert TZ to Pacific
    assgn.due_date = convert_to_pacific(assgn.due_date)
    assgn.lock_date = convert_to_pacific(assgn.lock_date)

    form = forms.AssignmentForm(obj=assgn)

    # TODO : Actually save updates.

    if assgn.course != current_course:
        return abort(401)

    return render_template('staff/course/assignment.html', assignment=assgn,
                           form=form, courses=courses,
                           current_course=current_course)

