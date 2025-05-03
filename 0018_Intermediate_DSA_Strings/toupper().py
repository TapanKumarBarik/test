"""
Problem Description

You are given a function to_upper() consisting of a character array A.

Convert each character of A into Uppercase character if it exists. If the Uppercase of a character does not exist, it remains unmodified.
The lowercase letters from a to z is converted to uppercase letters from A to Z respectively.

Return the uppercase version of the given character array.




Problem Constraints

1 <= |A| <= 105



Input Format

Only argument is a character array A.



Output Format

Return the uppercase version of the given character array.



Example Input

Input 1:

 A = ['S', 'c', 'A', 'L', 'E', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']
Input 2:

 A = ['S', 'c', 'a', 'L', 'e', 'R', '#', '2', '0', '2', '0']








Example Output

Output 1:

 ['S', 'C', 'A', 'L', 'E', 'R', 'A', 'C', 'A', 'D', 'E', 'M', 'Y']
Output 2:

 ['S', 'C', 'A', 'L', 'E', 'R', '#', '2', '0', '2', '0']








Example Explanation

Explanation 1:
 All the characters in the returned array are in uppercase alphabets.
Explanation 2:
 Since there is no Uppercase version for '#', '2'and '0'.  It remains unchanged.
 Rest of the Lowercase alphabets are converted to Uppercase accordingly.
"""

class Solution:
    # @param A : list of characters
    # @return a list of characters
    def to_upper(self, A):
        A =[x.upper() for x in A]
        return A

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    A1 = ['S', 'c', 'A', 'L', 'E', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']
    print(solution.to_upper(A1))  # Expected output: ['S', 'C', 'A', 'L', 'E', 'R', 'A', 'C', 'A', 'D', 'E', 'M', 'Y']

    # Test case 2
    A2 = ['S', 'c', 'a', 'L', 'e', 'R', '#', '2', '0', '2', '0']
    print(solution.to_upper(A2))  # Expected output: ['S', 'C', 'A', 'L', 'E', 'R', '#', '2', '0', '2', '0']