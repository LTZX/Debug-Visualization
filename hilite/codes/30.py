class Score(Resource):
    """ Score creation resource.
        Authenticated. Permissions: >= Staff
        Used by: Autograder
    """
    model = models.Score

