def isEmpty(obj):
    if obj is None:
        return True
    if isinstance(obj, str):
        if obj.isspace():
            return True
    return False
