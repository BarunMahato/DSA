class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ret = []
        nums.sort()
        for index, value in enumerate(nums):
            if value > 0:
                break
            if index > 0 and nums[index - 1] == value:
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[left] + nums[right] + value
                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    ret.append([value, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return ret