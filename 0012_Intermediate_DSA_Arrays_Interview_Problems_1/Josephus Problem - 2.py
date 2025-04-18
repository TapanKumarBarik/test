"""
Problem Description

There are A people standing in a circle. Person 1 kills their immediate clockwise neighbour and pass the knife to the next person standing in circle. This process continues till there is only 1 person remaining. Find the last person standing in the circle.



Problem Constraints

1 <= A <= 105


Input Format

First argument A is an integer.


Output Format

Return an integer.


Example Input

Input 1:
A = 4
Input 2:
A = 5


Example Output

Output 1:
1
Output 2:
3


Example Explanation

For Input 1:
Firstly, the person at position 2 is killed, then the person at position 4 is killed,
then the person at position 3 is killed. So the person at position 1 survives.
For Input 2:

Firstly, the person at position 2 is killed, then the person at position 4 is killed,
then the person at position 1 is killed. Finally, the person at position 5 is killed.
So the person at position 3 survives.
"""


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        power = 1
        while power * 2 <= A:
            power *= 2
        return 2 * (A - power) + 1

# Test the function
if __name__ == "__main__":
    solution = Solution()
    print(solution.solve(4))  # Output: 1
    print(solution.solve(5))  # Output: 3
    print(solution.solve(100))  # Output: 73

"""
Example Walkthrough
Input: A = 5
Largest power of 2 ≤ 5 is 4

So result = 2 * (5 - 4) + 1 = 3

Input: A = 4
Largest power of 2 ≤ 4 is 4

So result = 2 * (4 - 4) + 1 = 1
"""