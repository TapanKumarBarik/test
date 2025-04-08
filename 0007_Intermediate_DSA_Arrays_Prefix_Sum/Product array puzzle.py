"""
Given an array of integers A, find and return the product array of the same size where the ith element of the product array will be equal to the product of all the elements divided by the ith element of the array.

Note: It is always possible to form the product array with integer (32 bit) values. Solve it without using the division operator.


Input Format

The only argument given is the integer array A.
Output Format

Return the product array.
Constraints

2 <= length of the array <= 1000
1 <= A[i] <= 10
For Example

Input 1:
    A = [1, 2, 3, 4, 5]
Output 1:
    [120, 60, 40, 30, 24]

Input 2:
    A = [5, 1, 10, 1]
Output 2:
    [10, 50, 5, 50]
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        # [1, 2, 3, 4, 5]
        # 1,2,6,24,120
        # 120,120,60,20,5
        # answer
        #
        left_arr = [0] * len(A)
        right_arr = [0] * len(A)

        mul_l = 1
        mul_r = 1
        for i in range(len(A)):
            mul_l *= A[i]
            mul_r *= A[len(A) - 1 - i]

            left_arr[i] = mul_l
            right_arr[len(A) - 1 - i] = mul_r

        res_arr = [0] * len(A)

        for i in range(1, len(A) - 1, 1):
            res_arr[i] = left_arr[i - 1] * right_arr[i + 1]

        res_arr[0] = right_arr[1]
        res_arr[len(A) - 1] = left_arr[len(A) - 2]

        return res_arr

# Test cases
if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    sol = Solution()
    print(sol.solve(A))  # Output: [120, 60, 40, 30, 24]

    A = [5, 1, 10, 1]
    print(sol.solve(A))  # Output: [10, 50, 5, 50]