"""

Problem Description

You are given an integer A. You have to tell whether it is a perfect number or not.

Perfect number is a positive integer which is equal to the sum of its proper positive divisors.

A proper divisor of a natural number is the divisor that is strictly less than the number.








Problem Constraints

1 <= A <= 106



Input Format

First and only argument contains a single positive integer A.



Output Format

Return 1 if A is a perfect number and 0 otherwise.



Example Input

Input 1:

A = 4
Input 2:

A = 6


Example Output

Output 1:

0
Output 2:

1


Example Explanation

Explanation 1:

For A = 4, the sum of its proper divisors = 1 + 2 = 3, is not equal to 4.
Explanation 2:

For A = 6, the sum of its proper divisors = 1 + 2 + 3 = 6, is equal to 6.



Expected Output
Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
Arg 1: A single Integer, For e.g 9

"""


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A <= 1:
            return 0
        sum = 1
        i = 2
        while i * i <= A:
            if A % i == 0:
                sum += i
                sum += A / i
            i += 1

        if sum == A:
            return 1

        return 0
# # Example usage
solution = Solution()
A = 6  # Example input
print(solution.solve(A))  # Output: 1 (6 is a perfect number)
A = 4  # Example input
print(solution.solve(A))  # Output: 0 (4 is not a perfect number)
A = 28  # Example input
print(solution.solve(A))  # Output: 1 (28 is a perfect number)
A = 12  # Example input
print(solution.solve(A))  # Output: 0 (12 is not a perfect number)
A = 1  # Example input
print(solution.solve(A))  # Output: 0 (1 is not a perfect number)
A = 496  # Example input
print(solution.solve(A))  # Output: 1 (496 is a perfect number)
A = 8128  # Example input
print(solution.solve(A))  # Output: 1 (8128 is a perfect number)
A=120 # Example input
print(solution.solve(A))  # Output: 0 (120 is not a perfect number)