"""
Problem Description

Say you have an array, A, for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Return the maximum possible profit.



Problem Constraints

0 <= A.size() <= 700000



1 <= A[i] <= 107





Input Format

The first and the only argument is an array of integers, A.


Output Format

Return an integer, representing the maximum possible profit.


Example Input

Input 1:
A = [1, 2]
Input 2:

A = [1, 4, 5, 2, 4]


Example Output

Output 1:
1
Output 2:

4


Example Explanation

Explanation 1:
Buy the stock on day 0, and sell it on day 1.
Explanation 2:

Buy the stock on day 0, and sell it on day 2.
"""


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        buy_price = 99999999

        profit = 0

        for i in range(len(A)):
            if A[i] < buy_price:
                buy_price = A[i]

            if A[i] - buy_price > profit:
                profit = A[i] - buy_price

        return profit


# Test the function
if __name__ == "__main__":
    # Example input
    A = [1, 4, 5, 2, 4]

    # Create an instance of the Solution class
    solution = Solution()

    # Call the maxProfit method and print the result
    result = solution.maxProfit(A)
    print(result)  # Output: 4
    # Test with another example
    A = [1, 2]
    result = solution.maxProfit(A)
    print(result)  # Output: 1

# Improvements
