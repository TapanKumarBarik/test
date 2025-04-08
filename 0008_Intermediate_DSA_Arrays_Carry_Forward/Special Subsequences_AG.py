"""

Problem Description

You have given a string A having Uppercase English letters.

You have to find how many times subsequence "AG" is there in the given string.

NOTE: Return the answer modulo 109 + 7 as the answer can be very large.



Problem Constraints

1 <= length(A) <= 105



Input Format

First and only argument is a string A.



Output Format

Return an integer denoting the answer.



Example Input

Input 1:

 A = "ABCGAG"
Input 2:

 A = "GAB"


Example Output

Output 1:

 3
Output 2:

 0


Example Explanation

Explanation 1:

 Subsequence "AG" is 3 times in given string
Explanation 2:

 There is no subsequence "AG" in the given string.
"""


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        sum = 0
        count = 0

        for i in A:
            if i == "A":
                count += 1
            elif i == "G":
                sum += count
                sum %= 1000000007

        return sum


# Test Case
if __name__ == "__main__":
    A = "ABCGAG"
    obj = Solution()
    print(obj.solve(A))  # Output: 3

    A = "GAB"
    print(obj.solve(A))  # Output: 0