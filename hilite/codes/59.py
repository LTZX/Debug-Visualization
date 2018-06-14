@login_manager.request_loader
def load_user_from_request(request):
    token = request.args.get('access_token', None)
    if token is None:
        return None
    return user_from_access_token(token)

