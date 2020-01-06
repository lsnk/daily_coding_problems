from helpers import test_function


TEST_DATA = (
    (([10, 15, 3, 7], 19), False),
    (([10, 15, 3, 7], 18), True),
    (([10, 15, 3, 7], 17), True),
)


def check(l, k):
    values = set()

    for el in l:
        if k - el in values:
            return True
        values.add(el)

    return False


test_function(TEST_DATA, check)
