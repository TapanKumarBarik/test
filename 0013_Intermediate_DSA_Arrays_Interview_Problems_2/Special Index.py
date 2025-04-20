"""
Problem Description

Given an array, arr[] of size N, the task is to find the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.



Problem Constraints

1 <= N <= 105
-105 <= A[i] <= 105
Sum of all elements of A <= 109


Input Format

First argument contains an array A of integers of size N


Output Format

Return the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.



Example Input

Input 1:
A = [2, 1, 6, 4]
Input 2:

A = [1, 1, 1]






Example Output

Output 1:
1
Output 2:

3






Example Explanation

Explanation 1:
Removing arr[1] from the array modifies arr[] to { 2, 6, 4 } such that, arr[0] + arr[2] = arr[1].
Therefore, the required output is 1.
Explanation 2:

Removing arr[0] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
Removing arr[1] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
Removing arr[2] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
Therefore, the required output is 3.
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        even = []
        odd = []

        even_sum = 0
        odd_sum = 0

        for i in range(len(A)):

            if i % 2 == 0:
                # even
                even_sum += A[i]
            else:
                odd_sum += A[i]

            even.append(even_sum)
            odd.append(odd_sum)

        total_even = even[-1]
        total_odd = odd[-1]
        n = len(A) - 1
        count = 0
        for i in range(len(A)):

            # if we remove i then before i will remain as it is but
            # right side will change , even to odd and odd to even

            # remove i
            # 2, 1, 6, 4
            # even = 2,2,8,8
            # odd = 0,1,1,5
            # if we remove 0 even= 5 , odd = 6
            # if we remove 1 even = 2+ 5-1 , odd 0+8-2

            if i == 0:
                even_left = 0
                odd_left = 0
            else:
                even_left = even[i - 1]
                odd_left = odd[i - 1]

            even_right = total_odd - odd[i]
            odd_right = total_even - even[i]

            if even_left + even_right == odd_left + odd_right:
                count += 1

        return count





# Test cases
if __name__ == "__main__":
    # Test case 1
    A = [2, 1, 6, 4]
    solution = Solution()
    print(solution.solve(A))  # Output: 1

    # Test case 2
    A = [1, 1, 1]
    print(solution.solve(A))  # Output: 3
    # Test case 3
    A = [2, 1, 6, 4]
    print(solution.solve(A))  # Output: 1