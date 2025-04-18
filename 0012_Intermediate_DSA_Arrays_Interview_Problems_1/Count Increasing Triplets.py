"""
Problem Description

You are given an array A of N elements. Find the number of triplets i,j and k such that i<j<k and A[i]<A[j]<A[k]


Problem Constraints

1 <= N <= 103
1 <= A[i] <= 109


Input Format

First argument A is an array of integers.


Output Format

Return an integer.


Example Input

Input 1:
A = [1, 2, 4, 3]
Input 2:
A = [2, 1, 2, 3]


Example Output

Output 1:
2
Output 2:
1


Example Explanation

For Input 1:
The triplets that satisfy the conditions are [1, 2, 3] and [1, 2, 4].
For Input 2:

The triplet that satisfy the conditions is [1, 2, 3].
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        count = 0

        for i in range(len(A)):

            for j in range(i + 1, len(A)):
                if A[i] < A[j]:
                    for k in range(j + 1, len(A)):

                        if A[j] < A[k]:
                            count += 1

        return count



# Testthe function
if __name__ == "__main__":
    A = [1, 2, 4, 3]
    obj = Solution()
    print(obj.solve(A))  # Output: 2
    A = [2, 1, 2, 3]
    obj = Solution()
    print(obj.solve(A))  # Output: 1