def is_empty(obj):
    if obj is None:
        return True
    if isinstance(obj, str):
        if len(obj) == 0 or obj.isspace():
            return True
    return False


def empty_convert_none(s1: str):
    if is_empty(s1):
        return None
    return s1
