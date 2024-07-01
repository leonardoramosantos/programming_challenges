class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        result = False
        
        if x >= 0:
            loop_x = x
            loop_qtd = 0
            reversed_x = 0
            while loop_x > 0:
                reversed_x = reversed_x + (loop_x % 10) * (10 ** loop_qtd)
                loop_x = loop_x // 10
                loop_qtd = loop_qtd + 1
            print(reversed_x)
            result = reversed_x == x


        return result