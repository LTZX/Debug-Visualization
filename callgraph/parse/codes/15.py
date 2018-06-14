@admin.route("/")
@is_staff()
def index():
    courses, current_course = get_courses()
    if courses:
        return redirect(url_for(".course_assignments", cid=courses[0].id))
    return render_template('staff/index.html', courses=courses)


