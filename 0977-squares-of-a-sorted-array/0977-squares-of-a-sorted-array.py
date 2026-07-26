class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        if nums[0] > 0:
            return [n * n for n in nums]
        
        m = len(nums)
        for index, value in enumerate(nums):
            if value >= 0:
                m = index
                break
        
        A = nums[m:]
        B = [-1 * n for n in nums[:m][::-1]]
        def merge(A, B):
            a, b = 0, 0
            ret = []
            while a < len(A) and b < len(B):
                if A[a] < B[b]:
                    ret.append(A[a])
                    a += 1
                else:
                    ret.append(B[b])
                    b += 1
            if a < len(A):
                ret.extend(A[a:])
            else:
                ret.extend(B[b:])
            return ret
        sorted_array = merge(A, B)
        return [ n * n for n in sorted_array]