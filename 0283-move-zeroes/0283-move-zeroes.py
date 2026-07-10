class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num = [0] * len(nums)
        index = 0
        for n in nums:
            if n != 0:
                num[index] = n
                index += 1
        for i in range(len(nums)):
            nums[i] = num[i]