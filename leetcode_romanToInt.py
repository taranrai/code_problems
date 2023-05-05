
"""
Runtime
23 ms
Beats
98.54%
Memory
13.4 MB
Beats
58.26%
"""



class Solution:
    def romanToInt(self, s):
      roman_to_int_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

      summed_answer = 0
      for i in range(len(s)-1):
          if roman_to_int_dict[s[i]] < roman_to_int_dict[s[i+1]]:
              summed_answer -= roman_to_int_dict[s[i]]
          else:
              summed_answer += roman_to_int_dict[s[i]]

      return summed_answer + roman_to_int_dict[s[len(s)-1]]
