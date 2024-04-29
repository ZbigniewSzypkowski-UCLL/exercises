def process_data(string_data):
    return string_data.split(",")

def average_age(data):
    tot = 0
    for item in data:
        tot += item
    return tot / len(data)

def courses(data):
    return set(data)

def most_common_courses(data):
    return max(set(data), key = data.count)

# i surrender ;(