"""
191. Number of 1 Bits

Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

 

Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
"""


class Solution(object):
    def hammingWeight(self, n: int):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0

        while n != 0:
            if n & 1 == 1:
                cnt += 1
            n >>= 1

        print(cnt)


if __name__ == '__main__':
    s = Solution()
    s.hammingWeight(int(b'00000000000000000000000000001011', 2))
