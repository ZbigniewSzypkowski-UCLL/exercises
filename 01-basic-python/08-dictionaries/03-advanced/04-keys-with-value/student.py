def keys_with_value(dictionary, value):
    ans = list()
    for key, val in dictionary.items():
        if val == value:
            ans.append(key)
    return ans