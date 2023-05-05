'''
Runtime
55 ms
Beats
67.88%
Memory
13.3 MB
Beats
65.11%
'''


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        if x_str == x_str[::-1]:
            return True
        else:
            return False

