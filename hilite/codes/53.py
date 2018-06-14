    @wraps(func)
    def wrapper(*args, **kwargs):
        supplied = request.args.get('client_version', '')
        current_version, download_link = '2', ''  # TODO Actual Version Check
        if not supplied or supplied == current_version:
            return func(*args, **kwargs)

        message = ("Incorrect client version. Supplied version was {}. " +
                   "Correct version is {}.").format(supplied, current_version)
        data = {
            'supplied': supplied,
            'correct': current_version,
            'download_link': download_link
        }

        response = jsonify(**{
            'status': 403,
            'message': message,
            'data': data
        })
        response.status_code = 403
        return response
    return wrapper


