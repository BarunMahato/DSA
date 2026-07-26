class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = float('-inf')
        add = 0
        for num in nums:
            add += num
            if add > maxSum:
                maxSum = add
            if add < 0:
                add = 0
        return maxSum