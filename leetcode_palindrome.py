'''
Runtime
44 ms
Beats
91.54%
Memory
13.2 MB
Beats
99.23%
'''


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

