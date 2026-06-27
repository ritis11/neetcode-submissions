class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map ={}
        t_map = {}
        for char in s:
            if s_map.get(char, None) is None:
                s_map[char] = 1
            else:
                s_map[char] += 1
        for char in t:
            if t_map.get(char, None) is None:
                t_map[char] = 1
            else:
                t_map[char] += 1
        if s_map == t_map:
            return True
        return False
        