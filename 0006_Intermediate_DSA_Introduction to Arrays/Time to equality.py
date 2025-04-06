"""

Problem Description

Given an integer array A of size N. In one second, you can increase the value of one element by 1.

Find the minimum time in seconds to make all elements of the array equal.


Problem Constraints

1 <= N <= 1000000
1 <= A[i] <= 1000


Input Format

First argument is an integer array A.


Output Format

Return an integer denoting the minimum time to make all elements equal.


Example Input

A = [2, 4, 1, 3, 2]


Example Output

8


Example Explanation

We can change the array A = [4, 4, 4, 4, 4]. The time required will be 8 seconds.


"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max_num = max(A)
        sum = 0
        for num in A:
            sum += num

        return max_num * len(A) - sum


# Example usage
solution = Solution()
A = [2, 4, 1, 3, 2]
result = solution.solve(A)
print(result)  # Output: 8
A = [1, 2, 1]
solution = Solution()
print(solution.solve(A))  # Output: 0


# Thought Process
# 1. Find the maximum number in the array.
# 2. Calculate the sum of all elements in the array.
# 3. The time required to make all elements equal is the difference between the maximum number multiplied by the length of the array and the sum of all elements.
# 4. Return the result.
# 5. The time complexity of this solution is O(N), where N is the size of the array.