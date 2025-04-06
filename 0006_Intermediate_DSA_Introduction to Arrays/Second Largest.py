"""

Problem Description

You are given an integer array A. You have to find the second largest element/value in the array or report that no such element exists.


Problem Constraints

1 <= |A| <= 105


0 <= A[i] <= 109





Input Format

The first argument is an integer array A.





Output Format

Return the second largest element. If no such element exist then return -1.



Example Input

Input 1:

 A = [2, 1, 2]
Input 2:

 A = [2]


Example Output

Output 1:

 1
Output 2:

 -1


Example Explanation

Explanation 1:

 First largest element = 2
 Second largest element = 1
Explanation 2:

 There is no second largest element in the array.
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max_num=max(A)

        second_max=-1
        for num in A:
            if num!=max_num:
                second_max=max(num, second_max)

        return second_max
# Example Usage
if __name__ == "__main__":
    A = [2, 1, 2]
    solution = Solution()
    result = solution.solve(A)
    print(result)  # Output: 1
    A = [2]
    solution = Solution()
    result = solution.solve(A)
    print(result)  # Output: -1


# What i did
# 1. Find the maximum element in the array using the max() function.
# 2. Initialize a variable second_max to -1, which will store the second largest element.
# 3. Iterate through each element in the array A.
# 4. If the current element is not equal to the maximum element, update second_max to be the maximum of the current element and second_max.
# 5. Finally, return second_max, which will be the second largest element in the array. If no such element exists, it will return -1.
#