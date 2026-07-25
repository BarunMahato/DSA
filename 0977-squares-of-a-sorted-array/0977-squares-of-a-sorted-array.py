class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        if nums[0] >= 0:
            return [n * n for n in nums]
        
        m = len(nums) - 1
        for index, value in enumerate(nums):
            if value >= 0:
                m = index
                break
                
        A = nums[m:]
        B = nums[:m][::-1]
        B = [-1 * n for n in B]

        def merge(A, B):
            ret = []
            a, b = 0, 0
            while a < len(A) and b < len(B):
                if A[a] < B[b]:
                    ret.append(A[a])
                    a += 1
                else:
                    ret.append(B[b])
                    b += 1
            if a < len(A):
                ret.extend(A[a:])
            if b < len(B):
                ret.extend(B[b:])
            return ret
        merged_array =  merge(A, B)
        return [n * n for n in merged_array]
        