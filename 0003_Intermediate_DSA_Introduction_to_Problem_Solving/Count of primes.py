"""

Problem Description

You will be given an integer n. You need to return the count of prime numbers less than or equal to n.


Problem Constraints

0 <= n <= 10^3


Input Format

Single input parameter n in function.


Output Format

Return the count of prime numbers less than or equal to n.


Example Input

Input 1:
19
Input 2:
1


Example Output

Output 1:
8
Output 2:
0


Example Explanation

Explanation 1:
Primes <= 19 are 2, 3, 5, 7, 11, 13, 17, 19
Explanation 2:
There are no primes <= 1



Expected Output
Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
"""

class Solution:
    # @param A : integer
    # @return an integer

    def check_prime(self,n):
        i=2
        while i*i <=n:
            if n%i==0:
                return False

            i+=1

        return True

    def solve(self, A):
        count=0
        for i in range(2,A+1,1):
            if self.check_prime(i):
                count+=1
        return count



# Example usage
solution = Solution()
A = 19  # Example input
print(solution.solve(A))  # Output: 8
A = 1  # Example input
print(solution.solve(A))  # Output: 0
A = 0  # Example input
print(solution.solve(A))  # Output: 0
A = 2  # Example input
print(solution.solve(A))  # Output: 1
A = 3  # Example input
print(solution.solve(A))  # Output: 2
A = 4  # Example input
print(solution.solve(A))  # Output: 2
