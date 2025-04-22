"""
Problem Description

Given an array B of length A with elements 1 or 0. Find the number of subarrays such that the bitwise OR of all the elements present in the subarray is 1.
Note : The answer can be large. So, return type must be long.



Problem Constraints

1 <= A <= 105


Input Format

The first argument is a single integer A.
The second argument is an integer array B.


Output Format

Return the number of subarrays with bitwise array 1.


Example Input

Input 1:
 A = 3
B = [1, 0, 1]
Input 2:
 A = 2
B = [1, 0]


Example Output

Output 1:
5
Output2:
2


Example Explanation

Explanation 1:
The subarrays are :- [1], [0], [1], [1, 0], [0, 1], [1, 0, 1]
Except the subarray [0] all the other subarrays has a Bitwise OR = 1
Explanation 2:
The subarrays are :- [1], [0], [1, 0]
Except the subarray [0] all the other subarrays has a Bitwise OR = 1


"""


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an long
    def solve(self, A, B):
        N = A
        zero = 0
        count = 0

        for i in range(len(B)):
            if B[i] == 0:
                zero += 1
            else:
                count += (zero * (zero + 1)) // 2
                zero = 0

        count += (zero * (zero + 1)) // 2

        return (N * (N + 1)) // 2 - count

# Test the function
if __name__ == "__main__":
    A = 3
    B = [1, 0, 1]
    solution = Solution()
    result = solution.solve(A, B)
    print(result)  # Output: 5
    # Another test case
    A = 2
    B = [1, 0]
    result = solution.solve(A, B)
    print(result)  # Output: 2