class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target and i!=j:
                    return [i,j]
            i += 1 
        