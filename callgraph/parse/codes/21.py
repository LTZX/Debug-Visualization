class Backup(Resource):
    """ Submission retreival resource.
        Authenticated. Permissions: >= User/Staff
        Used by: Ok Client Submission/Exports.
    """
    schema = BackupSchema()
    model = models.Backup

