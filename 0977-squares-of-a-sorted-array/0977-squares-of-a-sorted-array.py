from collections import deque
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = collections.deque()
        left, right = 0, len(nums) - 1
        while left <= right:
            l, r = abs(nums[left]), abs(nums[right])
            if l > r:
                answer.appendleft(l * l)
                left += 1
            else:
                answer.appendleft(r * r)
                right -= 1
        return list(answer)