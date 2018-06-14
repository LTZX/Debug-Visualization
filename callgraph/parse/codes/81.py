def convert_to_utc(date):
    # TODO Not sure if 100% TZ aware. Unit test.
    return pytz.utc.localize(date)

