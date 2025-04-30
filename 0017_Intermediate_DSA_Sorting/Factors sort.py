"""
Problem Description

You are given an array A of N elements. Sort the given array in increasing order of number of distinct factors of each element, i.e., element having the least number of factors should be the first to be displayed and the number having highest number of factors should be the last one. If 2 elements have same number of factors, then number with less value should come first.

Note: You cannot use any extra space


Problem Constraints

1 <= N <= 104
1 <= A[i] <= 104


Input Format

First argument A is an array of integers.


Output Format

Return an array of integers.


Example Input

Input 1:
A = [6, 8, 9]
Input 2:
A = [2, 4, 7]


Example Output

Output 1:
[9, 6, 8]
Output 2:
[2, 7, 4]


Example Explanation

For Input 1:
The number 9 has 3 factors, 6 has 4 factors and 8 has 4 factors.
For Input 2:
The number 2 has 2 factors, 7 has 2 factors and 4 has 3 factors.

"""

import functools
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        def factor(num):
            count = 0
            i = 1
            while i*i<=num:
                if num%i==0 and i != num/i:
                    count += 2
                elif num%i==0 and i == num/i:
                    count += 1
                i += 1
            return count

        def compare(a,b):
            factor_a = factor(a)
            factor_b = factor(b)
            if factor_a != factor_b:
                return factor_a-factor_b
            else:
                return a-b
        return sorted(A,key=functools.cmp_to_key(compare))


# Test the function
if __name__ == "__main__":
    solution = Solution()
    A = [6, 8, 9]
    result = solution.solve(A)
    print(result)  # Output: [9, 6, 8]

    A = [2, 4, 7]
    result = solution.solve(A)
    print(result)  # Output: [2, 7, 4]