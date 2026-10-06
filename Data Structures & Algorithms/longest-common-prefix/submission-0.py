class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        mp = {}
        for word in strs:
            for idx in range(1, len(word) + 1):
                new_word = word[:idx]
                mp[new_word] = mp.get(new_word, 0) + 1
        
        res = ""
        for key, val in mp.items():
            if val == len(strs) and len(key) > len(res):
                res = key

        return res