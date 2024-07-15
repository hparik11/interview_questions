#!/usr/bin/env python
# coding:utf-8
"""
@FileName : 132_patten.py
@Author   : Harsh Parikh
@Date     : 10/2/21 12:00 AM

456. 132 Pattern

Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.



Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""


class Solution:
    def find132pattern(self, nums) -> bool:

        ## RC ##
        ## APPROACH : STACK ##
        ## LOGIC ##
        ## 1. We Create Minimum Array, till that position => O(n)
        ## 2. We start iterating from reverse of given array.
        ## 3. Remember we are using Stack and TopOfStack to determine, 2 in 132 pattern. ( so we have to check)
        ## 4. At any position, we push all elements IF greater than minimum (possible 2 in 132 pattern)
        ## 5. At any position, we pop all stack elements IF topOfStack is less or EQUAL to minimum (invalid element to form 132 pattern)
        ## 6. SATISFYING CONDITION : at any stage if min_nums[i] < stack[-1] < nums[i] we return True.

        ## TIME COMPLEXITY : O(N) ##
        ## SPACE COMPLEXITY : O(N) ##

        ## EDGE CASE : While checking the conditions 4,5,6. We should perform pop operation first i.e remove invalid elements before inserting the current element into the stack.

        if len(set(nums)) < 3:
            return False

        min_nums = [nums[0]]
        for i in range(1, len(nums)):
            min_nums.append(min(nums[i], min_nums[-1]))

        stack = []  # keep middle element 3 in 132
        print(min_nums)

        for i in range(len(nums) - 1, -1, -1):
            # find nums[i] to be 2 in 132
            if nums[i] < min_nums[i]:
                continue
            # 4
            if nums[i] > min_nums[i]:
                # 5
                while stack and stack[-1] <= min_nums[i]:
                    stack.pop()
                    print("here")

                # 6
                if stack and min_nums[i] < stack[-1] < nums[i]:
                    print(min_nums[i], stack[-1], nums[i])# return True
                # 4
                stack.append(nums[i])
            
            print(stack)

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.find132pattern([-1,3,2,0]))
