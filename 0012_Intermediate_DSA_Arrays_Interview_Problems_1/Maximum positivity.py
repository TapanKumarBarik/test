"""
Problem Description

Given an array of integers A, of size N.




Return the maximum size subarray of A having only non-negative elements. If there are more than one such subarray, return the one having the smallest starting index in A.

NOTE: It is guaranteed that an answer always exists.



Problem Constraints

1 <= N <= 105




-109 <= A[i] <= 109






Input Format

The first and only argument given is the integer array A.



Output Format

Return maximum size subarray of A having only non-negative elements. If there are more than one such subarrays, return the one having earliest starting index in A.



Example Input

Input 1:




 A = [5, 6, -1, 7, 8]


Input 2:

 A = [1, 2, 3, 4, 5, 6]







Example Output

Output 1:




 [5, 6]


Output 2:

 [1, 2, 3, 4, 5, 6]







Example Explanation

Explanation 1:




 There are two subarrays of size 2 having only non-negative elements.
 1. [5, 6]  starting point  = 0
 2. [7, 8]  starting point  = 3
 As starting point of 1 is smaller, return [5, 6]


Explanation 2:

 There is only one subarray of size 6 having only non-negative elements:
 [1, 2, 3, 4, 5, 6]
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        res1 = []
        final_res = []
        for i in range(len(A)):

            if A[i] > 0:
                res1.append(i)
            else:
                # NOW WE GOT -VE
                if len(res1) == len(final_res) and len(res1) > 0:
                    if res1[0] < final_res[0]:
                        final_res = res1.copy()

                elif len(res1) > len(final_res):
                    final_res = res1.copy()

                res1 = []

        if len(res1) > len(final_res):
            final_res = res1.copy()
        for i in range(len(final_res)):
            final_res[i] = A[final_res[i]]
        return final_res


# Test the function
if __name__ == "__main__":
    A = [5, 6, -1, 7, 8]
    obj = Solution()
    print(obj.solve(A))  # Output: [5, 6]
    A = [1, 2, 3, 4, 5, 6]
    obj = Solution()
    print(obj.solve(A))  # Output: [1, 2, 3, 4, 5, 6]
    A = [-1, -2, -3]
    obj = Solution()
    print(obj.solve(A))  # Output: []
    A = [1, 2, 3, -1, 4, 5]
    obj = Solution()
    print(obj.solve(A))  # Output: [1, 2, 3]