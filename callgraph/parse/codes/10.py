def convert_to_pacific(date):
    # TODO Move to UTILS
    return date.replace(tzinfo=pytz.utc)


