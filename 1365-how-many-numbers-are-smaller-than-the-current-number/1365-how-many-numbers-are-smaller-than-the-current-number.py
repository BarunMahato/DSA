class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        dictt = {}
        for index, num in enumerate(temp):
            if num not in dictt:
                dictt[num] = index
        ret = []
        for num in nums:
            ret.append(dictt[num])
        return ret
        