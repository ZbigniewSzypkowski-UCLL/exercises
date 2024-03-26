def word_count(string):
    tot = 0
    for char in string:
        if char != " ":
            tot += 1
    return tot