from intervals import overlapping_intervals


def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (5, 9))
    assert overlapping_intervals((3, 5), (4, 4))
    assert overlapping_intervals((1, 12), (3, 6))
    assert overlapping_intervals((3, 6), (1, 12))
    assert not overlapping_intervals((7, 10), (12, 19))
    assert not overlapping_intervals((12, 19), (7, 10))
    assert not overlapping_intervals((6, 3), (2, 5))