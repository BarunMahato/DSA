class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        longest = 0
        for index in range(1, len(arr) - 1):
            if arr[index - 1] < arr[index] > arr[index + 1]:
                left = right = index
                while left > 0 and arr[left] > arr[left - 1]:
                    left -= 1
                while right < len(arr) - 1 and arr[right] > arr[right + 1]:
                    right += 1
                longest = max(longest, right - left + 1)
        return longest