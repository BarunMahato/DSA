class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pCount, sCount = {}, {}
        for index in range(len(p)):
            pCount[p[index]] = 1 + pCount.get(p[index], 0)
            sCount[s[index]] = 1 + sCount.get(s[index], 0)
        ret = [0] if pCount == sCount else []
        left = 0
        for right in range(len(p), len(s)):
            sCount[s[right]] = 1 + sCount.get(s[right], 0)
            sCount[s[left]] -= 1
            if sCount[s[left]] == 0:
                sCount.pop(s[left])
            left += 1
            if sCount == pCount:
                ret.append(left)
        return ret