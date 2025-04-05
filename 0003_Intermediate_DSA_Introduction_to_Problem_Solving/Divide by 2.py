"""
What is the number of times we need to divide N by 2 till it reaches 1 ?
"""

"""
What is the number of times we need to divide N by 2 till it reaches 1 ?


In the question we are asked for number of times means exact number not the time complexity which tells how a particular solution or algorithm  scales not the exact number of executions.

Example 
1 operation is O(1)
100 operation is also O(1)
because O(1) means constant time 
1 is also constant and 100 is also constant 

but the number of operations that we have to do to get the result is different for both the cases despite having same time complexity O(1)

Now let’s switch back to question.
Number of Operations?
When N/2 → 1

Let’s do some dry run.

N = 2 
2/2 = 1
1 operation

N = 3
3/2 = 1
1 operation

N = 4
4/2 => 2/2 => 1
2 operation

N = 5
5/2 => 2/2 => 1
2 operation 

So if you observe
number of operations are incrementing on 2^m
m = 1,2,3,4,5,6…
For numbers lying between 2^m and 2^(m+1), number of operations remain same as 2^m.

log(n) base 2 produces whole number when n is 2^m and produces a decimal result lying in range of log(2^m) and log(2^(m+1)).
example 
m = 3
log(2^3) => log(8) => 3
log(2^4) => log(16) => 4

log(9) to log(15) will be 3.xxxx
But  operations can’t be fraction so we take only the whole part which is floor(log(N))

log(10) => 3.21
floor(log(10)) = 3

converting 10 to 1 by repeatedly diving by 2, takes O(log N) time complexity and takes 3 operations.

So final answer is we need to divide N, floor(log(N)) times.
"""