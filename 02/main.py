import operator
import timeit
from functools import reduce

from helpers import test_function


TEST_DATA = (
    (([1, 2, 3, 4, 5],), [120, 60, 40, 30, 24]),
    (([3, 2, 1],), [2, 3, 6]),
)


def result_with_division(l):
    total_product = reduce(operator.mul, l, 1)

    return [total_product/el for el in l]


def result_without_division_v1(l):
    values = frozenset(l)

    return [reduce(operator.mul, values - frozenset((el,)), 1) for el in l]


def result_without_division_v2(l):
    values = set(l)

    result = []
    for el in l:
        values.remove(el)
        result.append(reduce(operator.mul, values, 1))
        values.add(el)

    return result


def result_without_division_v3(l):

    result = []
    for el in l:
        result.append(reduce(operator.mul, (a for a in l if a != el), 1))

    return result


test_function(TEST_DATA, result_with_division)
test_function(TEST_DATA, result_without_division_v1)
test_function(TEST_DATA, result_without_division_v2)
test_function(TEST_DATA, result_without_division_v3)


# some speed testing

# with division
print(timeit.timeit(
    """result_with_division([1, 2, 3, 4, 5, 6])""", "from __main__ import result_with_division",  # ~0.0145
    number=10000
))

# without division v1
print(timeit.timeit(
    """result_without_division_v1([1, 2, 3, 4, 5, 6])""", "from __main__ import result_without_division_v1",  # ~0.07
    number=10000
))

# without division v2
print(timeit.timeit(
    """result_without_division_v2([1, 2, 3, 4, 5, 6])""", "from __main__ import result_without_division_v2",  # ~0.057
    number=10000
))

# without division v3
print(timeit.timeit(
    """result_without_division_v3([1, 2, 3, 4, 5, 6])""", "from __main__ import result_without_division_v3",  # ~0.085
    number=10000
))
