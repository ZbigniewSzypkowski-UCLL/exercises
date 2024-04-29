def overlapping_intervals(interval1, interval2):
    # Unpack bounds
    left1, right1 = interval1
    left2, right2 = interval2

    # Check if intervals overlap
    return (left1 <= right1 and left2 <= right2) and (left2 <= left1 <= right2 or left2 <= right1 <= right2 or left1 <= left2 <= right1 or left1 <= right2 <= right1)