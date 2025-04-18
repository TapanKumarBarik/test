"""
Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the longest consecutive 1’s that can be achieved.


Input Format

The only argument given is string A.
Output Format

Return the length of the longest consecutive 1’s that can be achieved.
Constraints

1 <= length of string <= 1000000
A contains only characters 0 and 1.
For Example

Input 1:
    A = "111000"
Output 1:
    3

Input 2:
    A = "111011101"
Output 2:
    7
"""

#TODO
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        total_1 = A.count('1')
        if total_1 == 0:
            return 0

        max_len = 0

        for i in range(len(A)):
            zero = 1
            curr_length = 0

            for j in range(i, len(A)):
                if A[j] == '1':
                    curr_length += 1
                else:
                    if zero == 0:
                        break
                    else:

                        if curr_length < total_1:
                            curr_length += 1
                            zero -= 1
                        else:
                            break

            max_len = max(max_len, min(curr_length, total_1))

        return max_len


#Test the function
if __name__ == "__main__":
    A = "111011101"
    obj = Solution()
    print(obj.solve(A))  # Output: 7
