class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ""
        max_length = 0

        curr_length = 0
        ind = 0
        for i in range(len(s)):
            if s[i] in s[i - curr_length:i]:
                max_length = curr_length if curr_length > max_length else max_length
                ind = s[i - curr_length:i].index(s[i])
                curr_length = curr_length - ind - 1
            
            curr_length = curr_length + 1
        
        return max_length if max_length > curr_length else curr_length