"""
Problem Description

Given an array A of N integers.
Count the number of elements that have at least 1 elements greater than itself.


Problem Constraints

1 <= N <= 105
1 <= A[i] <= 109


Input Format

First and only argument is an array of integers A.


Output Format

Return the count of elements.


Example Input

Input 1:
A = [3, 1, 2]
Input 2:
A = [5, 5, 3]


Example Output

Output 1:
2
Output 2:
1


Example Explanation

Explanation 1:
The elements that have at least 1 element greater than itself are 1 and 2
Explanation 2:
The elements that have at least 1 element greater than itself is 3

"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        ans = 0
        for i in range(len(A) - 1, 0, -1):
            # If the current element is not equal to the previous one,
            if A[i] != A[i - 1]:
                ans = i
                break
        return ans

    #Approch 2 without sorting
    def solve2(self, A):
        max_value = max(A)
        count = 0
        for num in A:
            if num < max_value:
                count += 1
        return count

# Test the function
if __name__ == "__main__":
    # Example test case
    A = [3, 1, 2]
    solution = Solution()
    result = solution.solve(A)
    print(result)  # Output: 2

    # Another test case
    B = [5, 5, 3]
    result = solution.solve(B)
    print(result)  # Output: 1

    #second method
    result = solution.solve2(B)
    print(result)  # Output: 1

# The above code defines a class Solution with two methods to solve the problem of counting elements in an array
# that have at least one element greater than themselves. The first method sorts the array and counts the elements,
# while the second method finds the maximum value and counts elements less than it without sorting.


#max(A) - will give max
# min(A) - will give min
#A.sort() - will sort the array