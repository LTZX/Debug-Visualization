def get_courses(cid=None):
    #  TODO : The decorator could add these to the routes
    enrollments = current_user.enrollments(roles=STAFF_ROLES)
    courses = [e.course for e in enrollments]
    matching_courses = [c for c in courses if c.id == cid]
    if not cid:
        return courses, []
    elif len(matching_courses) == 0:
        abort(401)  # TODO to actual error page
    current_course = matching_courses[0]
    return courses, current_course


