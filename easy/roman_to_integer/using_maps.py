class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        result = 0
        value_map = {}
        value_map["I"] = 1
        value_map["IV"] = 3
        value_map["V"] = 5
        value_map["IX"] = 8
        value_map["X"] = 10
        value_map["XL"] = 30
        value_map["L"] = 50
        value_map["XC"] = 80
        value_map["C"] = 100
        value_map["CD"] = 300
        value_map["D"] = 500
        value_map["CM"] = 800
        value_map["M"] = 1000

        last_subtract = ""
        for i in s:            
            result = result + (value_map[last_subtract + i] if last_subtract + i in value_map else value_map[i])
            
            print(result)

            if i in "IXC":
                last_subtract = i
            else:
                last_subtract = ""

        return result