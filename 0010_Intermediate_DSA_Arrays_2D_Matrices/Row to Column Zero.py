"""
Problem Description

You are given a 2D integer matrix A, make all the elements in a row or column zero if the A[i][j] = 0. Specifically, make entire ith row and jth column zero.



Problem Constraints

1 <= A.size() <= 103

1 <= A[i].size() <= 103

0 <= A[i][j] <= 103



Input Format

First argument is a 2D integer matrix A.



Output Format

Return a 2D matrix after doing required operations.



Example Input

Input 1:

[1,2,3,4]
[5,6,7,0]
[9,2,0,4]


Example Output

Output 1:

[1,2,0,0]
[0,0,0,0]
[0,0,0,0]


Example Explanation

Explanation 1:

A[2][4] = A[3][3] = 0, so make 2nd row, 3rd row, 3rd column and 4th column zero.
"""


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        n = len(A)

        row_arr = [1] * n
        col_arr = [1] * len(A[0])

        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    col_arr[j] = 0
                    row_arr[i] = 0

        for i in range(len(A)):
            for j in range(len(A[0])):
                if col_arr[j] == 0 or row_arr[i] == 0:
                    A[i][j] = 0

        return A

    def solve2_optimized(self, A):
        n = len(A)
        m = len(A[0])

        first_row_zero = False
        first_col_zero = False

        # Check if the first row has any zero
        for j in range(m):
            if A[0][j] == 0:
                first_row_zero = True
                break

        # Check if the first column has any zero
        for i in range(n):
            if A[i][0] == 0:
                first_col_zero = True
                break

        # Mark zeros in the first row and column
        for i in range(1, n):
            for j in range(1, m):
                if A[i][j] == 0:
                    A[i][0] = 0
                    A[0][j] = 0

        # Set rows to zero based on the first column
        for i in range(1, n):
            if A[i][0] == 0:
                for j in range(1, m):
                    A[i][j] = 0

        # Set columns to zero based on the first row
        for j in range(1, m):
            if A[0][j] == 0:
                for i in range(1, n):
                    A[i][j] = 0

        # Set the first row to zero if needed
        if first_row_zero:
            for j in range(m):
                A[0][j] = 0

        # Set the first column to zero if needed
        if first_col_zero:
            for i in range(n):
                A[i][0] = 0

        return A


# Test case
if __name__ == "__main__":
    A = [[1, 2, 3, 4],
         [5, 6, 7, 0],
         [9, 2, 0, 4]]
    obj = Solution()
    print(obj.solve(A))
    # Output: [[1, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    # Test case 2
    B = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    print(obj.solve(B))
    # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # Test case 3
    C = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    print(obj.solve(C))
    # Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # Test Optimized function
    print(obj.solve2_optimized(A))
    # Output: [[1, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    # Test case 2
    print(obj.solve2_optimized(B))
    # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


