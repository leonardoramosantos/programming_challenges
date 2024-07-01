class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        result = False

        if x >= 0:
            x_str = str(x)
            # finds the middle
            middle = len(x_str) // 2

            # gets left part and plus on digit if the number of digits is odd
            l = x_str[:middle + (1 if len(x_str) % 2 else 0)]
            # inverts the left part
            l = l[::-1]
            # gets right part
            r = x_str[middle:]

            print(l, r)

            result = l == r