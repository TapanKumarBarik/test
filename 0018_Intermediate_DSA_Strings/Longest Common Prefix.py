"""
Problem Description

Given the array of strings A, you need to find the longest string S, which is the prefix of ALL the strings in the array.


The longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".




Problem Constraints

0 <= sum of length of all strings <= 1000000



Input Format

The only argument given is an array of strings A.



Output Format

Return the longest common prefix of all strings in A.



Example Input

Input 1:


A = ["abcdefgh", "aefghijk", "abcefgh"]
Input 2:

A = ["abab", "ab", "abcd"];






Example Output

Output 1:

"a"
Output 2:

"ab"


Example Explanation

Explanation 1:

Longest common prefix of all the strings is "a".
Explanation 2:

Longest common prefix of all the strings is "ab".
"""

class Solution:
    # @param A : list of strings
    # @return a string
    def longestCommonPrefix(self, A):
        n = len(A)
        if n < 1:
            return ""
        prefix = A[0]
        prefixLen = len(prefix)
        for i in range(1, n):
            j = 0
            # finds the longest common prefix between A[i] and current prefix
            while j < min(prefixLen, len(A[i])):
                if prefix[j] != A[i][j]:
                    break
                j += 1
            if j < prefixLen:
                prefix = prefix[:j]
                prefixLen = j
        return prefix

# Test the function
if __name__ == "__main__":
    # Example usage
    solution = Solution()
    A = ["abcdefgh", "aefghijk", "abcefgh"]
    result = solution.longestCommonPrefix(A)
    print(result)  # Output: "a"
    # Example usage
    A2 = ["abab", "ab", "abcd"]
    result2 = solution.longestCommonPrefix(A2)
    print(result2)  # Output: "ab"