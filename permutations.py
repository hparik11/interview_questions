from typing import List


class Solution:
    def permuteAll(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, index, permutations):

            def swap(arr, i, j):
                arr[i], arr[j] = arr[j], arr[i]

            if index == len(nums) - 1:
                permutations.append(nums[:])
            else:
                for j in range(index, len(nums)):
                    swap(nums, index, j)
                    helper(nums, index + 1, permutations)
                    swap(nums, j, index)

        if not nums:
            return []

        permutations = []
        helper(sorted(nums[:]), 0, permutations)
        # print(permutations)
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

    def permute(self, nums):
        permutations = []

        if len(nums) <= 1:
            permutations.append(nums)
            return permutations

        # Take one element at a time from nums, and make permutations with the rest.
        for i in range(len(nums)):
            # # Avoid duplicate
            # if i > 0 and nums[i] == nums[i - 1]:
            #     continue
            # nums[:i] + nums[i+1:] is equivalent to nums without nums[i]
            print(nums[:i], nums[i + 1:])
            sub_permutations = self.permute(nums[:i] + nums[i + 1:])
            print(sub_permutations)
            for sub_permutation in sub_permutations:
                permutations.append([nums[i]] + sub_permutation)
        return permutations


if __name__ == "__main__":
    # s = Solution()
    # print(s.permuteAll([1, 2, 3]))

    s = Solution2()
    # print(s.permuteUnique([1, 1, 2]))
    print(s.permute([1, 2, 3]))
