"""

Problem Description

Given an integer A, you need to find the count of it's factors.

Factor of a number is the number which divides it perfectly leaving no remainder.

Example : 1, 2, 3, 6 are factors of 6


Problem Constraints

1 <= A <= 109


Input Format

First and only argument is an integer A.


Output Format

Return the count of factors of A.


Example Input

Input 1:
5
Input 2:
10


Example Output

Output 1:
2
Output 2:
4


Example Explanation

Explanation 1:
Factors of 5 are 1 and 5.
Explanation 2:
Factors of 10 are 1, 2, 5 and 10.



Expected Output
Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
Arg 1: A single Integer, For e.g 9
Enter Input Here

"""


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        count = 2
        i = 2
        while i * i <= A:
            if A % i == 0:
                if i * i == A:
                    count += 1
                else:
                    count += 2
            i += 1

        return count

# Example usage
if __name__ == "__main__":
    solution = Solution()
    A = 10  # Example input
    result = solution.solve(A)
    print(result)  # Output: 4
# The above code defines a class Solution with a method solve that counts the number of factors of a given integer A.