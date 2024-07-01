class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        result = False
        
        if x >= 0:
            # Count how many digits has the number
            ten_x = x
            ten_qtd = 1
            while ten_x >= 10:
                ten_x = ten_x // 10
                ten_qtd = ten_qtd + 1

            # Divide the numbers in two and reverse the right part
            r_number = 0
            l_number = x
            for i in range(ten_qtd // 2):
                r_number = r_number + ((l_number % 10) * (10 ** ((ten_qtd // 2) - i - 1)))
                l_number = l_number / 10

            # If the qtd of numbers is odd, deletes the middle digit
            if ten_qtd % 2:
                l_number = l_number / 10

            return l_number == r_number
                

        return result