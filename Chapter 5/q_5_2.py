import os
import unittest


# Basic recursive solution


def binaryTostring(input):
    # check is input is teween 0 to 1
    if input < 0 or input > 1:
        return False

    res, ex, pre = "0.", 1, 0

    while input > 0:
        tm = 0.5 ** ex
        while tm > input:
            ex += 1
            tm = tm * 0.5
        input -= tm

        # how many 0s
        zeros = ex - 1 - pre

        res += ('0' * zeros) + '1'

        # update divisor or substractor since ex was updated more than 1 step
        pre = ex
        ex += 1
        if len(res) > 34:
            break

    return float(res) if len(res) <= 34 else "ERROR"


class Test(unittest.TestCase):

    tests = [
        (0.625, 0.101),
        (0.74, "ERROR"),
    ]

    def test_is_route(self):
        for [input, output] in self.tests:
            actual = binaryTostring(input)
            assert actual == output


if __name__ == "__main__":
    unittest.main()
