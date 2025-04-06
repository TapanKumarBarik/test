"""

Problem Description

 You are given an integer array A of length N.
 You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
 For each query, you have to find the sum of all elements from L to R indices in A (0 - indexed).
 More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.


Problem Constraints

 1 <= N, M <= 103
 1 <= A[i] <= 105
 0 <= L <= R < N


Input Format

The first argument is the integer array A.
The second argument is the 2D integer array B.


Output Format

 Return an integer array of length M where ith element is the answer for ith query in B.


Example Input

Input 1:


A = [1, 2, 3, 4, 5]
B = [[0, 3], [1, 2]]
Input 2:

A = [2, 2, 2]
B = [[0, 0], [1, 2]]




Example Output

Output 1:
[10, 5]
Output 2:

[2, 4]


Example Explanation

Explanation 1:


The sum of all elements of A[0 ... 3] = 1 + 2 + 3 + 4 = 10.
The sum of all elements of A[1 ... 2] = 2 + 3 = 5.
Explanation 2:

The sum of all elements of A[0 ... 0] = 2 = 2.
The sum of all elements of A[1 ... 2] = 2 + 2 = 4.



"""


class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        suf_arr = []
        sum = 0
        for num in A:
            sum += num
            suf_arr.append(sum)

        # [1, 2, 3, 4, 5]
        # [1,3,6,10,15]
        # 0,3 - A[3] 10 as 0
        # 1,2 - A[2]-A[0]

        res_arr = []
        for arr in B:
            left = arr[0]
            right = arr[1]
            if left != 0:
                res_arr.append(suf_arr[right] - suf_arr[left - 1])
            else:
                res_arr.append(suf_arr[right])

        return res_arr


# Example Usage
A = [1, 2, 3, 4, 5]
B = [[0, 3], [1, 2]]
solution = Solution()
result = solution.solve(A, B)
print(result)  # Output: [10, 5]
A = [2, 2, 2]
B = [[0, 0], [1, 2]]
solution = Solution()
result = solution.solve(A, B)
print(result)  # Output: [2, 4]

# thought process
# 1. Create a suffix array to store the cumulative sum of elements in A.
# 2. Iterate through the elements of A and calculate the cumulative sum.
# 3. For each query in B, calculate the sum of elements from index L to R using the suffix array.
# 4. If L is not 0, subtract the cumulative sum at index L-1 from the cumulative sum at index R.
# 5. If L is 0, simply return the cumulative sum at index R.
# 6. Return the results for all queries as a list.
# 7. The time complexity of this approach is O(N + M), where N is the length of A and M is the number of queries.
