


def box_mapping(column, row):
    if column < 3:
        if row < 3:
            return 0
        if row < 6:
            return 1
        return 2
    if column < 6:
        if row < 3:
            return 3
        if row < 6:
            return 4
        return 5
    if row < 3:
        return 6
    if row < 6:
        return 7
    return 8
