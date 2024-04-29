def double_dict_values(d):
    new_dict = {}
    for key, value in d.items():
        new_dict[key] = value * 2
    return new_dict