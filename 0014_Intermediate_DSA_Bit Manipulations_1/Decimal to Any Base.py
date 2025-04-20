"""
Problem Description

Given a decimal number A and a base B, convert it into its equivalent number in base B.


Problem Constraints

0 <= A <= 512
2 <= B <= 10


Input Format

The first argument will be decimal number A.
The second argument will be base B.


Output Format

Return the conversion of A in base B.


Example Input

Input 1:
A = 4
B = 3
Input 2:
A = 4
B = 2


Example Output

Output 1:
11
Output 2:
100


Example Explanation

Explanation 1:
Decimal number 4 in base 3 is 11.
Explanation 2:
Decimal number 4 in base 2 is 100.
"""


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def DecimalToAnyBase(self, A, B):
        res = 0
        multiplier = 1
        while A > 0:
            temp = A % B * multiplier
            multiplier *= 10
            res += temp
            A = A // B

        return res


# Test the function
if __name__ == "__main__":
    A = 4
    B = 3
    solution = Solution()
    result = solution.DecimalToAnyBase(A, B)
    print(result)  # Output: 11
     # Test with another input
    A = 4
    B = 2
    result = solution.DecimalToAnyBase(A, B)
    print(result)  # Output: 100