"""
Problem Description

Given an array A. Sort this array using Count Sort Algorithm and return the sorted array.


Problem Constraints

1 <= |A| <= 105
1 <= A[i] <= 105


Input Format

The first argument is an integer array A.


Output Format

Return an integer array that is the sorted array A.


Example Input

Input 1:
A = [1, 3, 1]
Input 2:
A = [4, 2, 1, 3]


Example Output

Output 1:
[1, 1, 3]
Output 2:
[1, 2, 3, 4]


Example Explanation

For Input 1:
The array in sorted order is [1, 1, 3].
For Input 2:
The array in sorted order is [1, 2, 3, 4].

"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        mx = max(A)
        freq = [0 for j in range(mx + 1)]
        for x in A:
            freq[x] += 1
        ans = []
        for i in range(mx + 1):
            for j in range(freq[i]):
                ans.append(i)
        return ans


# Test the function
if __name__ == "__main__":
    # Example input
    A = [4, 2, 1, 3]

    # Create an instance of the Solution class
    solution = Solution()

    # Call the solve method and print the result
    sorted_array = solution.solve(A)
    print(sorted_array)  # Output: [1, 2, 3, 4]