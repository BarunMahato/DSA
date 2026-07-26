from collections import deque
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = collections.deque()
        left = 0
        right = len(nums) - 1
        while left <= right:
            numLeft , numRight = abs(nums[left]), abs(nums[right])
            if numLeft < numRight:
                answer.appendleft(numRight * numRight)
                right -= 1
            else:
                answer.appendleft(numLeft * numLeft)
                left += 1
        return list(answer)