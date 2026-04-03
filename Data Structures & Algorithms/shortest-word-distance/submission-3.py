class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
       
        word1idx = word2idx = -1

        minDistance = len(wordsDict)

        for idx,word in enumerate(wordsDict):
            if word == word1:
                word1idx = idx
            if word == word2:
                word2idx = idx
            if word1idx != -1 and word2idx != -1:
                minDistance = min(minDistance,abs(word2idx-word1idx))
        
        return minDistance