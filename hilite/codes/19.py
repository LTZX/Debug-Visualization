        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user.is_authenticated:
                roles = current_user.enrollments(roles=STAFF_ROLES)
                if len(roles) > 0 or current_user.is_admin:
                    if course_arg:
                        course = kwargs[course_arg]
                        if course in [r.course.id for r in roles]:
                            return func(*args, **kwargs)
                    else:
                        return func(*args, **kwargs)
            flash("You are not on the course staff", "error")
            return redirect(url_for("student.index"))
        return wrapper
    return decorator


