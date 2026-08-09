class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        positiveIndex = len(nums)
        for index, num in enumerate(nums):
            if num >= 0:
                positiveIndex = index
                break
        A = nums[positiveIndex:]
        B = [ - 1 * n for n in nums[:positiveIndex][::-1]]

        a = 0
        b = 0
        ret = []
        while a < len(A) and b < len(B):
            if A[a] > B[b]:
                ret.append(B[b])
                b += 1
            else:
                ret.append(A[a])
                a += 1
        if a < len(A):
            ret.extend(A[a:])
        if b < len(B):
            ret.extend(B[b:])
        ret = [n * n for n in ret]
        return ret
