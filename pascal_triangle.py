from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final_array = []
        
        for i in range(1, numRows+1):
            sub_array = []
            for j in range(1, i+1):
                if j == 1 or j == i:
                    sub_array.append(1)
                else:
                    sub_array.append(final_array[i-2][j-1] + final_array[i-2][j-2])
            final_array.append(sub_array)

        return (final_array)

if __name__ == "__main__":
    print(Solution().generate(5))