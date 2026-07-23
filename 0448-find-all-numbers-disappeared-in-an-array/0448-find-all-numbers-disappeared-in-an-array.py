class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ret = []
        set_nums = set(nums)
        for num in range(1, len(nums)  + 1):
            if num not in set_nums:
                ret.append(num)
        return ret