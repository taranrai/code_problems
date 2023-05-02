def sum(n):
   if n == 1:
       return 0
   return n + sum(n-1)

a = sum(5)
print(a)


# output is 14

"""
When the function is called with the argument 5, it first checks whether 5 == 1. 
Since that is not true, the function returns 5 + sum(4). 
The sum(4) call results in 4 + sum(3), which results in 3 + sum(2), which results in 2 + sum(1). 
At this point, the function sum returns 0 because the argument n is 1.

So, the final result of calling sum(5) is 5 + 4 + 3 + 2 + 0, which is 14. 
Therefore, when the code prints the value of a, it outputs 14.
"""
