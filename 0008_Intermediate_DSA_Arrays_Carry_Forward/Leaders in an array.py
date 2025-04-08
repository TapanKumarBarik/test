"""
Problem Description

Given an integer array A containing N distinct integers, you have to find all the leaders in array A. An element is a leader if it is strictly greater than all the elements to its right side.

NOTE: The rightmost element is always a leader.


Problem Constraints

1 <= N <= 105
1 <= A[i] <= 108


Input Format

There is a single input argument which a integer array A


Output Format

Return an integer array denoting all the leader elements of the array.


Example Input

Input 1:
 A = [16, 17, 4, 3, 5, 2]
Input 2:
 A = [5, 4]


Example Output

Output 1:
[17, 2, 5]
Output 2:
[5, 4]


Example Explanation

Explanation 1:
 Element 17 is strictly greater than all the elements on the right side to it.
 Element 2 is strictly greater than all the elements on the right side to it.
 Element 5 is strictly greater than all the elements on the right side to it.
 So we will return these three elements i.e [17, 2, 5], we can also return [2, 5, 17] or [5, 2, 17] or any other ordering.
Explanation 2:
 Element 5 is strictly greater than all the elements on the right side to it.
 Element 4 is strictly greater than all the elements on the right side to it.
 So we will return these two elements i.e [5, 4], we can also any other ordering.
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        res=[]
        max_num=0
        for i in range(len(A)-1,0,-1):
            if A[i]>max_num:
                max_num=A[i]
                res.append(max_num)

        return res

# Test the function
if __name__ == "__main__":
    A = [16, 17, 4, 3, 5, 2]
    solution = Solution()
    result = solution.solve(A)
    print(result)  # Output: [17, 2, 5]
    A = [5, 4]
    solution = Solution()
    result = solution.solve(A)
    print(result)  # Output: [5, 4]