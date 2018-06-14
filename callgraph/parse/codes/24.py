class Enrollment(PublicResource):
    """ View what courses students are enrolled in.
        Authenticated. Permissions: >= User
        Used by: Ok Client Auth
    """
    model = models.Participant
    schema = EnrollmentSchema()

