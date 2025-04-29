"""
Problem Description

Given an integer A representing a year, Return 1 if it is a leap year else, return 0.

A year is a leap year if the following conditions are satisfied:

The year is multiple of 400.
or the year is multiple of 4 and not multiple of 100.

Problem Constraints

1 <= A <= 109



Input Format

First and only argument is an integer A



Output Format

Return 1 if it is a leap year else return 0



Example Input

Input 1

 A = 2020
Input 2:

 A = 1999


Example Output

Output 1

 1
Output 2:

 0


Example Explanation

Explanation 1

 2020 is a leap year.
 2020 is not a multiple of 400 but it is divisible by 4 and also at the same time not divisible by 100.
Explanation 2:

 1999 is not a leap year.
 199 is not a multiple of 400. It is not divisible by 4 and also at the same time not divisible by 100.
 All the conditions fail.
"""

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if (A%400==0) or (A%4==0 and A%100!=0):
            return 1
        return 0


# Test the function
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Test case 1
    A1 = 2020
    result1 = solution.solve(A1)
    print(f"Test case 1: A = {A1}, Result = {result1}")  # Expected output: 1

    # Test case 2
    A2 = 1999
    result2 = solution.solve(A2)
    print(f"Test case 2: A = {A2}, Result = {result2}")  # Expected output: 0