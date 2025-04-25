"""
Problem Description

Given an integer A, find and return the Ath magic number.

A magic number is defined as a number that can be expressed as a power of 5 or a sum of unique powers of 5.

First few magic numbers are 5, 25, 30(5 + 25), 125, 130(125 + 5), ….



Problem Constraints

1 <= A <= 5000



Input Format

The only argument given is integer A.



Output Format

Return the Ath magic number.



Example Input

Example Input 1:

 A = 3
Example Input 2:

 A = 10


Example Output

Example Output 1:

 30
Example Output 2:

 650


Example Explanation

Explanation 1:

 Magic Numbers in increasing order are [5, 25, 30, 125, 130, ...]
 3rd element in this is 30
Explanation 2:

 In the sequence shown in explanation 1, 10th element will be 650.
"""


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        result = 0
        power = 1

        while A > 0:
            if A & 1:
                result += pow(5, power)
            power += 1
            A >>= 1

        return result

# Test case
if __name__ == "__main__":
    A = 3
    obj = Solution()
    print(obj.solve(A))  # Output: 30

    A = 10
    print(obj.solve(A))  # Output: 650