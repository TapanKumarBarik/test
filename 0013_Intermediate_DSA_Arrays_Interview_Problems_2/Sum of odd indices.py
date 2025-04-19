"""
Problem Description

You are given an array A of length N and Q queries given by the 2D array B of size Q*2. Each query consists of two integers B[i][0] and B[i][1].
For every query, the task is to calculate the sum of all odd indices in the range A[B[i][0]…B[i][1]].

Note : Use 0-based indexing


Problem Constraints

1 <= N <= 105
1 <= Q <= 105
1 <= A[i] <= 100
0 <= B[i][0] <= B[i][1] < N


Input Format

First argument A is an array of integers.
Second argument B is a 2D array of integers.


Output Format

Return an array of integers.


Example Input

Input 1:
A = [1, 2, 3, 4, 5]
B = [   [0,2]
        [1,4]   ]
Input 2:
A = [2, 1, 8, 3, 9]
B = [   [0,3]
        [2,4]   ]


Example Output

Output 1:
[2, 6]
Output 2:
[4, 3]


Example Explanation

For Input 1:
The subarray for the first query is [1, 2, 3] whose sum of odd indices is 2.
The subarray for the second query is [2, 3, 4, 5] whose sum of odd indices is 6.
For Input 2:
The subarray for the first query is [2, 1, 8, 3] whose sum of odd indices is 4.
The subarray for the second query is [8, 3, 9] whose sum of odd indices is 3.


"""

class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):

        num_to_add = []

        odd = []

        sum = 0
        for i in range(len(A)):
            if i % 2 != 0:
                # even
                sum += A[i]
            odd.append(sum)

        for i in range(len(B)):
            start = B[i][0]
            end = B[i][1]

            if start == 0:
                num_to_add.append(odd[end])
            else:
                num_to_add.append(odd[end] - odd[start - 1])

        return num_to_add

# Test the function
if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    B = [[0, 2], [1, 4]]
    obj = Solution()
    print(obj.solve(A, B))  # Output: [2, 6]

    A = [2, 1, 8, 3, 9]
    B = [[0, 3], [2, 4]]
    obj = Solution()
    print(obj.solve(A, B))  # Output: [4, 3]