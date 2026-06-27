class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        left = 0
        ls = 0
        for i, c in enumerate(s):
            if c in hm and hm[c] >= left:
                left = hm[c] + 1
            hm[c] = i
            ls = max(ls, i - left + 1)
        return ls



        ## LONGEST STRING WIHOUT REPEATITION in STRS: 
        # hashmap={}
        # for idx, val in enumerate(s):
        #     if hashmap.get(val) is None:
        #         hashmap[val] = idx
        #     else:
        #         return (idx)      