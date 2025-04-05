"""

Problem Description

Given a number A. Return square root of the number if it is perfect square otherwise return -1.

Note: A number is a perfect square if its square root is an integer.

Problem Constraints

1 <= A <= 108
Input Format

First and the only argument is an integer A.
Output Format

Return an integer which is the square root of A if A is perfect square otherwise return -1.
Example Input

Input 1:
A = 4
Input 2:

A = 1001
Example Output

Output 1:
2
Output 2:

-1
Example Explanation

Explanation 1:
sqrt(4) = 2
Explanation 2:

1001 is not a perfect square.
Expected Output
Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
Arg 1: A single Integer, For e.g 9
Enter Input Here

"""

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        i=1
        while i*i<=A:
            if A%i==0:
                if i*i==A:
                    return i

            i+=1
        return -1

# Example usage
sol = Solution()
print(sol.solve(4))  # Output: 2
print(sol.solve(9))  # Output: 3
print(sol.solve(16))  # Output: 4
print(sol.solve(25))  # Output: 5
print(sol.solve(36))  # Output: 6
print(sol.solve(49))  # Output: 7
print(sol.solve(1001))  # Output: -1
