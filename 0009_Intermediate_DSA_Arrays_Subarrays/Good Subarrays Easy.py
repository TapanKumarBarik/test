"""
Problem Description

Given an array of integers A, a subarray of an array is said to be good if it fulfills any one of the criteria:
1. Length of the subarray is be even, and the sum of all the elements of the subarray must be less than B.
2. Length of the subarray is be odd, and the sum of all the elements of the subarray must be greater than B.
Your task is to find the count of good subarrays in A.


Problem Constraints

1 <= len(A) <= 5 x 103
1 <= A[i] <= 103
1 <= B <= 107


Input Format

The first argument given is the integer array A.
The second argument given is an integer B.


Output Format

Return the count of good subarrays in A.


Example Input

Input 1:
A = [1, 2, 3, 4, 5]
B = 4
Input 2:

A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
B = 65


Example Output

Output 1:
6
Output 2:

36


Example Explanation

Explanation 1:
Even length good subarrays = {1, 2}
Odd length good subarrays = {1, 2, 3}, {1, 2, 3, 4, 5}, {2, 3, 4}, {3, 4, 5}, {5}
Explanation 1:
There are 36 good subarrays
"""


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0

        for i in range(len(A)):
            arr_size = 0
            temp_sum = 0

            for j in range(i, len(A)):

                arr_size += 1
                temp_sum += A[j]

                if arr_size % 2 == 0:
                    if temp_sum < B:
                        count += 1

                else:
                    if temp_sum > B:
                        count += 1

        return count

# Test the function
if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    B = 4
    solution = Solution()
    result = solution.solve(A, B)
    print(result)  # Output: 6
# Test the function with another example
    A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
    B = 65
    result = solution.solve(A, B)
    print(result)  # Output: 36