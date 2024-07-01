class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        majority = -1
        qtd_of_majority = 0
        # Create a list of tested elements to avoid
        # re-processing the same number multiple times
        tested_items = []
        for i in nums:
            if i not in tested_items:
                tested_items.append(i)
                qtd_element = nums.count(i)
                if qtd_element > qtd_of_majority:
                    qtd_of_majority = qtd_element
                    majority = i

        return majority