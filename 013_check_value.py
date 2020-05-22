def is_falsy(value):
    if value:
        return 'True'
    elif bool(value):
        return 'True'
    else:
        return 'False'