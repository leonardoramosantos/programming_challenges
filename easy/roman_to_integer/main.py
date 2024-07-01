class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        result = 0

        last_subtract = ""
        for i in s:
            if i == "I":
                result = result + 1
            elif i == "V":
                result = result + 5 - (2 if last_subtract == "I" else 0)
            elif i == "X":
                result = result + 10 - (2 if last_subtract == "I" else 0)
            elif i == "L":
                result = result + 50 - (20 if last_subtract == "X" else 0)
            elif i == "C":
                result = result + 100 - (20 if last_subtract == "X" else 0)
            elif i == "D":
                result = result + 500 - (200 if last_subtract == "C" else 0)
            elif i == "M":
                result = result + 1000 - (200 if last_subtract == "C" else 0)
            
            print(result)

            if i in ["I", "X", "C"]:
                last_subtract = i
            else:
                last_subtract = ""

        return result