class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for n in range(0, len(nums)-1):
            if nums[n] == nums[n+1]:
                return True
        return False
