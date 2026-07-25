class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_Diff = float('inf')
        for index in range(1, len(arr)):
            min_Diff = min(min_Diff, arr[index] - arr[index - 1])
        ret = []
        for index in range(1, len(arr)):
            if (arr[index] - arr[index - 1] == min_Diff):
                ret.append([arr[index-1], arr[index]])
        return ret