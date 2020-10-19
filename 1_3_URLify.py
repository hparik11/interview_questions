import unittest


def urlify(urlString, length):
    url = ''
    for index in range(length):
        if urlString[index] == ' ':
            url += '%20'
        else:
            url += urlString[index]
    return url


class Test(unittest.TestCase):
    """Test Cases"""
    # Using lists because Python strings are immutable
    data = [
        ('much ado about nothing      ', 22, 'much%20ado%20about%20nothing'),
        ('Mr John Smith    ', 13, 'Mr%20John%20Smith')]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            print(actual)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
