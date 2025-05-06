"""
Problem Description

Given a string A, you are asked to reverse the string and return the reversed string.



Problem Constraints

1 <= |A| <= 105

String A consist only of lowercase characters.



Input Format

First and only argument is a string A.



Output Format

Return a string denoting the reversed string.



Example Input

Input 1:

 A = "scaler"
Input 2:

 A = "academy"


Example Output

Output 1:

 "relacs"
Output 2:

 "ymedaca"

"""
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        n = len(A)
        ans = ""
        for i in range(n-1, -1, -1):
            ans += A[i]
        return ans

# Test the function

if __name__ == "__main__":
    # Example usage
    solution = Solution()
    A = "scaler"
    result = solution.solve(A)
    print(result)  # Output: "relacs"