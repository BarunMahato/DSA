class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = max_sum = nums[0]
        for index in range(1, len(nums)):
            current_sum = max(nums[index], current_sum + nums[index])
            max_sum = max(current_sum, max_sum)
        return max_sum