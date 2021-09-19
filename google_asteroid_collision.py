"""
735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.



Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
Example 4:

Input: asteroids = [-2,-1,1,2]
Output: [-2,-1,1,2]
Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving right. Asteroids moving the same direction never meet, so no asteroids will meet each other.
"""


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for astroid in asteroids:
            if not stack:
                stack.append(astroid)
            else:
                curr = astroid
                collide = False
                while stack and stack[-1] > 0 and curr < 0:
                    # Both asteroids are equal, destroy both.
                    if abs(curr) == abs(stack[-1]):
                        stack.pop()
                        collide = True

                        break

                    # Stack top is bigger, remove the +ve asteroid
                    # from the stack and replace current with top.
                    elif abs(curr) < abs(stack[-1]):
                        curr = stack.pop()

                    # Stack top is smaller than current, remove the +ve asteroid
                    # from the stack.
                    elif abs(curr) > abs(stack[-1]):
                        stack.pop()

                if not collide:
                    stack.append(curr)

        return stack
