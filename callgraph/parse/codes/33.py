def authenticate(func):
    """ Provide user object to API methods. Passes USER as a keyword argument
        to all protected API Methods.
    """
