"""

Problem Description

Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array

and at least one occurrence of the minimum value of the array.



Problem Constraints

1 <= |A| <= 2000



Input Format

First and only argument is vector A



Output Format

Return the length of the smallest subarray which has at least one occurrence of minimum and maximum element of the array



Example Input

Input 1:

A = [1, 3, 2]
Input 2:

A = [2, 6, 1, 6, 9]


Example Output

Output 1:

 2
Output 2:

 3


Example Explanation

Explanation 1:

 Take the 1st and 2nd elements as they are the minimum and maximum elements respectievly.
Explanation 2:

 Take the last 3 elements of the array.
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        min_value = min(A)
        max_value = max(A)

        if max_value == min_value:
            return 1

        min_length = len(A)

        for i in range(len(A) - 1):
            if A[i] == min_value:
                # find next max value

                for j in range(i + 1, len(A), 1):

                    if A[j] == max_value:
                        min_length = min(min_length, j - i + 1)
                        break

            elif A[i] == max_value:
                # find next min value
                for j in range(i + 1, len(A), 1):
                    if A[j] == min_value:
                        min_length = min(min_length, j - i + 1)
                        break

        return min_length

# Test the function
if __name__ == "__main__":
    solution = Solution()
    A = [1, 3, 2]
    print(solution.solve(A))  # Output: 2
    A = [2, 6, 1, 6, 9]
    print(solution.solve(A))  # Output: 3
    A = [1, 1, 1]
    print(solution.solve(A))  # Output: 1