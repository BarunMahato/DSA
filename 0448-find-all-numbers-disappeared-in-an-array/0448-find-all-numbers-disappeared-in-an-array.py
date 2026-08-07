class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        unique_nums = set(nums)
        ret = []
        for num in range(1, len(nums) + 1):
            if num not in unique_nums:
                ret.append(num)
        return ret