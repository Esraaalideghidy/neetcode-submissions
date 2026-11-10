class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for index, value in enumerate(nums):
            complement = target - value

            if complement in numbers :
                return [numbers[complement],index]
            numbers[value]=index
