class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        uniqueNum = set(nums)
        ret = []
        for num in range(1, len(nums) + 1):
            if num not in uniqueNum:
                ret.append(num)
        return ret