import unittest


def twoSum(input_array, target):
    i, j = 0, len(input_array) - 1

    while i < j:
        temp_sum = input_array[i] + input_array[j]
        if temp_sum == target:
            return input_array[i], input_array[j]
        elif temp_sum < target:
            i += 1
        else:
            j -= 1

    return "Not available"


class Test1(unittest.TestCase):
    dataT = [([-1, 2, 3, 4, 5, 6, 7], 12)]


    def test_unique(self):
        # true check
        for test_array, target in self.dataT:
            actual = twoSum(test_array, target)
            print(actual)
            self.assertEqual(actual, (5, 7))
        # false check
        # for test_string in self.dataF:
        #     actual = twoSum(test_string)
        #     self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
