class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNum = sorted(nums)
        numMap = {}
        for index, num in enumerate(sortedNum):
            if num not in numMap:
                numMap[num] = index
        ret = []
        for num in nums:
            ret.append(numMap[num])
        return ret