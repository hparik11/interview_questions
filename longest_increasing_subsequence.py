from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    size = len(nums)
    if size == 0:
        return 0
    subs = [(0, 0)] * size
    subs[0] = (1, float('-inf'))
    final_max = float('-inf')

    for i in range(1, size):
        maximum = 0
        parent = float('-inf')
        for j in range(0, i):
            if nums[j] < nums[i] and maximum < subs[j][0]:
                maximum, parent = subs[j][0], nums[j]
        if final_max < maximum + 1:
            final_max = maximum + 1
        subs[i] = (maximum + 1, parent)

    # i = len(subs) - 1
    # j = i - 1
    # seqs = []
    # while j > 0:
    #     # print(subs[i][0])
    #     if subs[j][0] == subs[i][0] - 1:
    #         i -= 1
    #         if len(seqs) == 0:
    #             seqs.insert(0, nums[i])
    #         seqs.insert(0, nums[i - 1])
    #
    #         if final_max == len(seqs):
    #             break
    #     j -= 1
    # print(nums)
    # print(seqs)
    return final_max


if __name__ == "__main__":
    # print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    # print(lengthOfLIS([5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]))
    print(lengthOfLIS([10, 22, 9, 33, 21, 61, 41, 60, 80]))
    print(lengthOfLIS([1, 5, -1, 10]))
