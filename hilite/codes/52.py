    @wraps(func)
    def wrapper(*args, **kwargs):
        # Public methods do not need authentication
        if not getattr(func, 'public', False) and not current_user.is_authenticated:
            restful.abort(401)
        kwargs['user'] = current_user
        return func(*args, **kwargs)
    return wrapper


