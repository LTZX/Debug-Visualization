def json_field(field):
    """
    Parses field or list, or returns appropriate boolean value.

    :param field: (string)
    :return: (string) parsed JSON
    """
    if not field[0] in ['{', '[']:
        if field == 'false':
            return False
        elif field == 'true':
            return True
        return field
    return json.loads(field)


