class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for i in range(1, len(nums)):
            if nums[left] == 0 and nums[i] != 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            elif nums[left] != 0:
                left += 1
        return nums
