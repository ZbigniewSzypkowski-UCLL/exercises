def merge_dicts(d1, d2):
    new_dict = d1
    for key, value in d2.items():
        new_dict[key] = value
    return new_dict
    