vertices = [
    # (x in m, y in m)
    (-3, -3),
    (0, 0), (0, 11.89-6.40), (0, 11.89),
    (1.37, 0), (1.37, 11.89-6.40), (1.37, 11.89),
    (10.97-1.37, 0), (10.97-1.37, 11.89-6.40), (10.97-1.37, 11.89),
    (10.97, 0), (10.97, 11.89-6.40), (10.97, 11.89),
    (10.97/2, 11.89-6.40), (10.97/2, 11.89),
]

partial_lines = [
    (1, 2), (2, 3), (1, 4), (4, 5), (5, 6), (4, 7), (7, 8), (8, 9), (7, 10),
    (10, 11), (11, 12), (5, 13), (8, 13), (13, 14),
]

full_lines = [
    (1, 3), (1, 10), (4, 6), (7, 9),
    (10, 12), (5, 8), (13, 14),
]

test0 = [
    (1, 2),
]

test1 = [
    (1, 2), (3, 4),
]
