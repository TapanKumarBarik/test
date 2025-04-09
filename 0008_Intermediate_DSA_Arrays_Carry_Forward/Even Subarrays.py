"""
Problem Description

You are given an integer array A.

Decide whether it is possible to divide the array into one or more subarrays of even length such that the first and last element of all subarrays will be even.

Return "YES" if it is possible; otherwise, return "NO" (without quotes).



Problem Constraints

1 <= |A|, A[i] <= 106



Input Format

The first and the only input argument is an integer array, A.



Output Format

Return a string "YES" or "NO" denoting the answer.



Example Input

Input 1:

 A = [2, 4, 8, 6]
Input 2:

 A = [2, 4, 8, 7, 6]


Example Output

Output 1:

 "YES"
Output 2:

 "NO"


Example Explanation

Explanation 1:

 We can divide A into [2, 4] and [8, 6].
Explanation 2:

 There is no way to divide the array into even length subarrays.
"""

class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):

        #FIRST CONDITION
        if len(A)%2!=0:
            return "NO"

        #SECOND CONDITION
        elif A[0]%2!=0:
            return "NO"

        #THIRED CONDITION
        elif A[len(A)-1]%2!=0:
            return "NO"


        return "YES"

# Test the function
if __name__ == "__main__":
    # Example test case
    A = [2, 4, 8, 6]
    solution = Solution()
    result = solution.solve(A)
    print(result)  # Output: "YES"

    # Another test case
    B = [2, 4, 8, 7, 6]
    result = solution.solve(B)
    print(result)  # Output: "NO"