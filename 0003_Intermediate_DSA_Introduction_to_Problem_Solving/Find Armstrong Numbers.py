"""

Problem Description

You are given an integer A. You need to print all the Armstrong Numbers between 1 to A.

If sum of cubes of each digit of the number is equal to the number itself, then the number is called an Armstrong number.

For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 ).



Problem Constraints

1 <= N <= 500



Input Format

First and only argument is an integer A.



Output Format

Return an integer array of all the Armstrong numbers in range [1,A].



Example Input

Input 1:

 5
Input 2:

 200


Example Output

Output 1:

1
Output 2:

[1, 153]


Example Explanation

Explanation 1:

1 is an armstrong number.
Explanation 2:

1 and 153 are armstrong number under 200.
"""

class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):

        arr=[]
        for i in range (1,A+1,1):
            sum=0
            B=i
            j=i
            while j>0:
                last_num=j%10
                j=j//10
                temp_sum = last_num*last_num*last_num
                sum+=temp_sum

            if sum==B:
                arr.append(i)
        return arr




#Example Usage
solution = Solution()
A = 200  # Example input
print(solution.solve(A))  # Output: [1, 153]
A = 5  # Example input
print(solution.solve(A))  # Output: [1]
A = 500  # Example input
print(solution.solve(A))  # Output: [1, 153]