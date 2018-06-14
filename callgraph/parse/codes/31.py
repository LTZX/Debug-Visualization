class Submission(Resource):
    """ Submission resource.
        Authenticated. Permissions: >= Student/Staff
        Used by: Ok Client Submission.
    """
    model = models.Submission
    schema = SubmissionSchema()

