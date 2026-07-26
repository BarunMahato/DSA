class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = float('inf')
        for index in range(1, len(arr)):
            minDiff = min(minDiff, arr[index] - arr[index - 1])
        ret = []
        for index in range(1, len(arr)):
            if arr[index] - arr[index - 1] == minDiff:
                ret.append([arr[index - 1], arr[index]])
        return ret