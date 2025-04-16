"""
Problem Description

Given an array A of size N, find the subarray of size B with the least average.



Problem Constraints

1 <= B <= N <= 105
-105 <= A[i] <= 105


Input Format

First argument contains an array A of integers of size N.
Second argument contains integer B.


Output Format

Return the index of the first element of the subarray of size B that has least average.
Array indexing starts from 0.


Example Input

Input 1:
A = [3, 7, 90, 20, 10, 50, 40]
B = 3
Input 2:

A = [3, 7, 5, 20, -10, 0, 12]
B = 2






Example Output

Output 1:
3
Output 2:

4






Example Explanation

Explanation 1:
Subarray between indexes 3 and 5
The subarray {20, 10, 50} has the least average
among all subarrays of size 3.
Explanation 2:

 Subarray between [4, 5] has minimum average





"""


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        min_sum = 0

        for i in range(B):
            min_sum += A[i]

        i = 0
        j = B

        start_index = 0
        temp_sum = min_sum
        while j < len(A):
            temp_sum -= A[i]
            temp_sum += A[j]

            if min_sum > temp_sum:
                min_sum = temp_sum
                start_index = i + 1

            i += 1
            j += 1

        return start_index

# Test case
if __name__ == "__main__":
    A = [3, 7, 90, 20, 10, 50, 40]
    B = 3
    solution = Solution()
    result = solution.solve(A, B)
    print(result)  # Output: 3
    # Test case
    A = [3, 7, 5, 20, -10, 0, 12]
    B = 2
    solution = Solution()
    result = solution.solve(A, B)
    print(result)  # Output: 4