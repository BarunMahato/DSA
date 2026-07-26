class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNum = sorted(nums)
        indexMap = {}
        for index, num in enumerate(sortedNum):
            if num not in indexMap:
                indexMap[num] = index
        ret = []
        for num in nums:
            ret.append(indexMap[num])
        return ret