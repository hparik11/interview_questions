class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        final_string = ''
        print(s.split(' '))
        for word in s.split(' '):
            final_string += word[::-1] + " "
        return final_string.rstrip()
        

if __name__ == '__main__':
    s = Solution()
    s.reverseWords("Let's take LeetCode contest")