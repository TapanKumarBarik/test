"""
Problem Description

You're given a read-only array of N integers. Find out if any integer occurs more than N/3 times in the array in linear time and constant additional space.
If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Note: Read-only array means that the input array should not be modified in the process of solving the problem



Problem Constraints

1 <= N <= 7*105
1 <= A[i] <= 109


Input Format

The only argument is an integer array A.


Output Format

Return an integer.


Example Input

Input 1:
[1 2 3 1 1]
Input 2:
[1 2 3]


Example Output

Output 1:
1
Output 2:
-1


Example Explanation

Explanation 1:
1 occurs 3 times which is more than 5/3 times.
Explanation 2:
No element occurs more than 3 / 3 = 1 times in the array.


"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A)
        if n == 0:
            return -1

        # 1st pass: find up to two candidates
        cand1, cand2 = None, None
        count1, count2 = 0, 0
        for x in A:
            if cand1 == x:
                count1 += 1
            elif cand2 == x:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = x, 1
            elif count2 == 0:
                cand2, count2 = x, 1
            else:
                count1 -= 1
                count2 -= 1

        # 2nd pass: verify actual counts
        count1 = sum(1 for x in A if x == cand1)
        count2 = sum(1 for x in A if x == cand2)

        if count1 > n // 3:
            return cand1
        if count2 > n // 3:
            return cand2
        return -1

# Test the function
if __name__ == "__main__":
    solution = Solution()
    # Example 1
    A = [1, 2, 3, 1, 1]
    print(solution.repeatedNumber(A))  # Output: 1

    # Example 2
    A = [1, 2, 3]
    print(solution.repeatedNumber(A))  # Output: -1