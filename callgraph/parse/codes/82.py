def strip_whitespace(value):
    if value and hasattr(value, "strip"):
        return value.strip()
    else:
        return value


