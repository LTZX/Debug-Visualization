def make_backup(user, assignment, messages, submit, submitter):
    """
    Create backup with message objects.

    :param user: (object) caller
    :param assignment: (Assignment)
    :param messages: Data content of backup/submission
    :param submit: Whether this backup is a submission to be graded
    :param submitter: (object) caller or submitter
    :return: (Backup) backup
    """

    analytics = messages.get('analytics')

    if analytics:
        # message_date = analytics.get('time', None)
        client_time = datetime.datetime.now()
        # TODO client_time = parse_date(message_date)
    else:
        client_time = datetime.datetime.now()

    backup = models.Backup(client_time=client_time, submitter=user.id,
                           assignment=assignment.id, submit=submit)
    messages = [models.Message(kind=k, backup=backup,
                contents=m) for k, m in messages.iteritems()]
    backup.messages = messages
    models.db.session.add_all(messages)
    models.db.session.add(backup)
    models.db.session.commit()
    return backup


