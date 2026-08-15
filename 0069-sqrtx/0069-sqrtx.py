class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left = 1
        right = int(x / 2)
        ans = 0
        while left <= right:
            mid = int(left + ( right - left) /2)
            if (mid <= x / mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans