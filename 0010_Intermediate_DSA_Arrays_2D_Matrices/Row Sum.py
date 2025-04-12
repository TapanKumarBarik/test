"""
Problem Constraints

1 <= A.size() <= 103

1 <= A[i].size() <= 103

1 <= A[i][j] <= 103



Input Format

First argument A is a 2D array of integers.(2D matrix).



Output Format

Return an array containing row-wise sums of original matrix.



Example Input

Input 1:

[1,2,3,4]
[5,6,7,8]
[9,2,3,4]


Example Output

Output 1:

[10,26,18]


Example Explanation

Explanation 1

Row 1 = 1+2+3+4 = 10
Row 2 = 5+6+7+8 = 26
Row 3 = 9+2+3+4 = 18

"""


class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        res = []

        for i in range(len(A)):
            sum = 0
            for j in range(len(A[0])):
                sum += A[i][j]
            res.append(sum)

        return res

# Time Complexity: O(N^2)
# Space Complexity: O(N)
# where N is the number of rows and M is the number of columns in the matrix.
# The time complexity is O(N^2) because we are iterating through each element of the matrix once.
# The space complexity is O(N) because we are using a list to store the row sums, which has a size of N.
#Test
if __name__ == "__main__":
    A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 2, 3, 4]]
    obj = Solution()
    print(obj.solve(A)) # Output: [10, 26, 18]
    #Ex2
    A = [[1, 2], [3, 4], [5, 6]]
    obj = Solution()
    print(obj.solve(A)) # Output: [3, 7, 11]