import unittest


def unique(string):
    if len(string) > 128:
        return False

    uniqueChars = [False for _ in range(128)]

    for each in string:
        if uniqueChars[ord(each)]:
            return False
        else:
            uniqueChars[ord(each)] = True

    return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()