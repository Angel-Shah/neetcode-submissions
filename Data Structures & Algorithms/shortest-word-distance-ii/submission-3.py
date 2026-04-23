class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.hashmap = {}
        for idx,word in enumerate(wordsDict):
            if word not in self.hashmap:
                self.hashmap[word] = [idx]
            else:
                self.hashmap[word].append(idx)

    def shortest(self, word1: str, word2: str) -> int:
        w1Indicies = self.hashmap[word1]
        w2Indicies = self.hashmap[word2]
        p1 = p2 = 0
        minDist = float('inf')
        while p1<len(w1Indicies) and p2<len(w2Indicies):
            minDist = min(minDist,abs(w1Indicies[p1] - w2Indicies[p2]))

            if w1Indicies[p1] < w2Indicies[p2]:
                p1 += 1
            else:
                p2 +=1
        return minDist

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
