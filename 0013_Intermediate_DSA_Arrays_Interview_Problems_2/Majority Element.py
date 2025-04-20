"""
Problem Description

Given an array of size N, find the majority element. The majority element is the element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exists in the array.



Problem Constraints

1 <= N <= 5*105
1 <= num[i] <= 109


Input Format

Only argument is an integer array.


Output Format

Return an integer.


Example Input

Input 1:
[2, 1, 2]
Input 2:
[1, 1, 1]


Example Output

Input 1:
2
Input 2:
1


Example Explanation

For Input 1:
2 occurs 2 times which is greater than 3/2.
For Input 2:
 1 is the only element in the array, so it is majority

"""


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        maj = 0
        maj_count = 0

        for i in range(len(A)):

            if maj_count == 0:
                maj = A[i]
                maj_count = 1
            elif maj != A[i]:
                if maj_count > 0:
                    maj_count -= 1
            elif maj == A[i]:
                maj_count += 1

        return maj





# #Test the function
if __name__ == "__main__":
    A = [2, 1, 2]
    B = [1, 1, 1]
    obj = Solution()
    print(obj.majorityElement(A))  # Output: 2
    print(obj.majorityElement(B))  # Output: 1
