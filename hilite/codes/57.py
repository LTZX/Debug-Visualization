@google_auth.tokengetter
def google_oauth_token(token=None):
    return session.get('google_token', None)

