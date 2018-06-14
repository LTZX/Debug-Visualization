@admin.route("/course/<int:cid>/assignments")
@is_staff(course_arg='cid')
def course_assignments(cid):
    courses, current_course = get_courses(cid)
    assgns = current_course.assignments
    active_asgns = [a for a in assgns if a.active]
    due_asgns = [a for a in assgns if not a.active]
    # TODO CLEANUP : Better way to send this data to the template.

    return render_template('staff/course/assignments.html',
                           courses=courses, current_course=current_course,
                           active_asgns=active_asgns, due_assgns=due_asgns)


