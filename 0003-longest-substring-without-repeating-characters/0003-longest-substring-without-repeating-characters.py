class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        sett = set()
        longest = 0
        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1
            window_length = right - left + 1
            longest = max(longest, window_length)
            sett.add(s[right])
        return longest