class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetDict = {}
        for index, value in enumerate(nums):
            compliment = target - value
            if compliment in targetDict:
                return index, targetDict[compliment]
            targetDict[value] = index