class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()

        for idx, word in enumerate(words):
            for i in range(len(words)):
                if idx == i:
                    continue
                if word in words[i]:
                    res.add(word)

        return list(res)