class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        new_list = []
        counter = 0
        for i in nums:
            if i == 1 :
                counter +=1
            if i == 0 :
                new_list.append(counter)
                counter = 0
        new_list.append(counter)
        return max(new_list)
               