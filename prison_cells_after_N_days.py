# -*- coding: utf-8 -*-
# @Author: hparikh
# @FileName: prison_cells_after_N_days.py
# @Date:   10/3/20, Sat
"""
Prison Cells After N Days
Medium

785

1065

Add to List

Share
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)



Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation:
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]
"""
from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        pattern = set()
        count = 0
        flag_found = False
        for _ in range(N):
            temp = cells[:]
            for i in range(0, len(cells)):
                if i == 0 or i == len(cells) - 1:
                    cells[i] = 0
                else:
                    if temp[i - 1] == temp[i + 1]:
                        cells[i] = 1
                    else:
                        cells[i] = 0

            cell_tuple = tuple(cells)
            if cell_tuple in pattern:
                flag_found = True
                break

            pattern.add(cell_tuple)

            count += 1
        if flag_found:
            return self.prisonAfterNDays(cells, (N - 1) % count)
        return cells


if __name__ == '__main__':
    s = Solution()
    print(s.prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 7) == [0, 0, 1, 1, 0, 0, 0, 0])
    print(s.prisonAfterNDays([1, 0, 0, 1, 0, 0, 1, 0], 1000000000) == [0, 0, 1, 1, 1, 1, 1, 0])
