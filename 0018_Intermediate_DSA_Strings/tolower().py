"""
Problem Description

You are given a function to_lower() which takes a character array A as an argument.




Convert each character of A into lowercase characters if it exists. If the lowercase of a character does not exist, it remains unmodified.
The uppercase letters from A to Z are converted to lowercase letters from a to z respectively.

Return the lowercase version of the given character array.






Problem Constraints

1 <= |A| <= 105



Input Format

The only argument is a character array A.



Output Format

Return the lowercase version of the given character array.



Example Input

Input 1:

 A = ['S', 'c', 'A', 'l', 'e', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']
Input 2:

 A = ['S', 'c', 'a', 'L', 'e', 'r', '#', '2', '0', '2', '0']


Example Output

Output 1:

 ['s', 'c', 'a', 'l', 'e', 'r', 'a', 'c', 'a', 'd', 'e', 'm', 'y']
Output 2:

 ['s', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']


Example Explanation

Explanation 1:

 All the characters in the returned array are in lowercase alphabets.
Explanation 2:
 Since there is no lowercase version for '#', '2'and '0'.  It remains unchanged.
 Rest of the Uppercase alphabets are converted to lowercase accordingly.

"""

class Solution:
    # @param A : list of characters
    # @return a list of characters
    def to_lower(self, A):
        A = [x.lower() for x in A]
        return A


# Example usage
if __name__ == "__main__":
    solution = Solution()
    input1 = ['S', 'c', 'A', 'l', 'e', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']
    output1 = solution.to_lower(input1)
    print(output1)  # Expected output: ['s', 'c', 'a', 'l', 'e', 'r', 'a', 'c', 'a', 'd', 'e', 'm', 'y']

    input2 = ['S', 'c', 'a', 'L', 'e', 'r', '#', '2', '0', '2', '0']
    output2 = solution.to_lower(input2)
    print(output2)  # Expected output: ['s', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']