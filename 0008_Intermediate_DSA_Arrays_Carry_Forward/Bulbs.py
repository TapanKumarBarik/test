"""
Problem Description

A wire connects N light bulbs.


Each bulb has a switch associated with it; however, due to faulty wiring, a switch also changes the state of all the bulbs to the right of the current bulb.

Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs.

You can press the same switch multiple times.

Note: 0 represents the bulb is off and 1 represents the bulb is on.




Problem Constraints

0 <= N <= 5×105
0 <= A[i] <= 1



Input Format

The first and the only argument contains an integer array A, of size N.



Output Format

Return an integer representing the minimum number of switches required.



Example Input

Input 1:

 A = [0, 1, 0, 1]
Input 2:

 A = [1, 1, 1, 1]


Example Output

Output 1:

 4
Output 2:

 0


Example Explanation

Explanation 1:

 press switch 0 : [1 0 1 0]
 press switch 1 : [1 1 0 1]
 press switch 2 : [1 1 1 0]
 press switch 3 : [1 1 1 1]
Explanation 2:

 There is no need to turn any switches as all the bulbs are already on.
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        operation_done=0
        count=0
        for bulb in A:
            if bulb == 0:
                #off
                if operation_done %2 == 0:
                    #even
                    operation_done+=1
                    count+=1
                else:
                    #odd means off could be on so can be skipped
                    pass
            else:
                #was on initially
                if operation_done%2==0:
                    #there should be no changhe
                    pass
                else:
                    operation_done+=1
                    count+=1
        return count

# Test the function
if __name__ == "__main__":
    # Example test case
    A = [0, 1, 0, 1]
    solution = Solution()
    result = solution.bulbs(A)
    print(result)  # Output: 4
    # Test with another example
    A = [1, 1, 1, 1]
    result = solution.bulbs(A)
    print(result)  # Output: 0


