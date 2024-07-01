class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ""
        max_length = 0

        curr_length = 0
        for i in s:
            if i in substr:
                max_length = curr_length if curr_length > max_length else max_length
                substr = substr[substr.index(i) + 1:]
                curr_length = len(substr)
            
            curr_length = curr_length + 1
            substr = substr + i
            print(substr)
        
        return max_length if max_length > curr_length else curr_length