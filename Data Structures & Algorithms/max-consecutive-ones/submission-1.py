class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_count = 0
        for i in nums:
            if i == 1 :
                counter +=1
                max_count = max(max_count, counter)
            if i == 0 :
                counter = 0
        return max_count
               