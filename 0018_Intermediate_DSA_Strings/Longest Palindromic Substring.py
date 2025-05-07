
"""
Problem Description

Given a string A of size N, find and return the longest palindromic substring in A.

Substring of string A is A[i...j] where 0 <= i <= j < len(A)

Palindrome string:
A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.

Incase of conflict, return the substring which occurs first ( with the least starting index).



Problem Constraints

1 <= N <= 6000



Input Format

First and only argument is a string A.



Output Format

Return a string denoting the longest palindromic substring of string A.



Example Input

Input 1:
A = "aaaabaaa"
Input 2:
A = "abba


Example Output

Output 1:
"aaabaaa"
Output 2:
"abba"


Example Explanation

Explanation 1:
We can see that longest palindromic substring is of length 7 and the string is "aaabaaa".
Explanation 2:
We can see that longest palindromic substring is of length 4 and the string is "abba".
"""


class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        aLen = len(A)
        if aLen == 0:
            return A
        A2 = "|"
        for x in A:
            A2 += x + "|"
        p = [0] * (2 * aLen + 1)
        c = 0
        r = 0
        m = 0
        n = 0
        for i in range(1, 2 * aLen + 1):
            if i > r:
                p[i] = 0
                m = i - 1
                n = i + 1
            else:
                i2 = c * 2 - i
                if p[i2] < r - i:
                    p[i] = p[i2]
                    m = -1
                else:
                    p[i] = r - i
                    n = r + 1
                    m = i * 2 - n
            while m >= 0 and n < 2 * aLen + 1 and A2[m] == A2[n]:
                p[i] += 1
                m -= 1
                n += 1
            if i + p[i] > r:
                c = i
                r = i + p[i]
        leng = 0
        c = 0
        for i in range(1, 2 * aLen + 1):
            if leng < p[i]:
                leng = p[i]
                c = i
        ret = A2[c - leng + 1 : c + leng + 1 : 2]
        return ret



# Test the function
if __name__ == "__main__":
    # Example usage
    solution = Solution()
    A = "aaaabaaa"
    result = solution.longestPalindrome(A)
    print(result)  # Output: "aaabaaa"

    A2 = "abba"
    result2 = solution.longestPalindrome(A2)
    print(result2)  # Output: "abba"
