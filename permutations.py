from typing import List


class Solution:
    def permuteAll(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, index, permutations):

            if index == len(nums) - 1:
                permutations.append(nums[:])
            else:
                for j in range(index, len(nums)):
                    swap(nums, index, j)
                    helper(nums, index + 1, permutations)
                    swap(nums, j, index)

        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        if not nums:
            return []

        permutations = []
        nums_done = set()
        helper(sorted(nums[:]), 0, permutations)
        print(permutations)
        return permutations


class Solution2:
    def permuteUnique(self, nums):
        nums.sort()
        return self.permuteUniqueSorted(nums)

    def permuteUniqueSorted(self, nums):
        permutations = []

        if len(nums) <= 1:
            permutations.append(nums)
            return permutations

        # Take one element at a time from nums, and make permutations with the rest.
        for i in range(len(nums)):
            # Avoid duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # nums[:i] + nums[i+1:] is equivalent to nums without nums[i]
            sub_permutations = self.permuteUniqueSorted(nums[:i] + nums[i + 1:])
            print(sub_permutations)
            for sub_permutation in sub_permutations:
                permutations.append([nums[i]] + sub_permutation)
        return permutations


if __name__ == "__main__":
    s = Solution()
    print("kjsdlkfjsl")
    print(s.permuteAll([1, 2, 3]))

    s = Solution2()
    print("kjsdlkfjsl")
    print(s.permuteUnique([1, 1, 2]))
