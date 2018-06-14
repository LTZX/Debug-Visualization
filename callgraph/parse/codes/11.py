@admin.route("/course/<int:cid>")
@is_staff(course_arg='cid')
def course(cid):
    return redirect(url_for(".course_assignments", cid=cid))
    #courses, current_course = get_courses(cid)
    #return render_template('staff/course/index.html',
    #                       courses=courses, current_course=current_course)


