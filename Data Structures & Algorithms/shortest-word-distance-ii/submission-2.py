class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.hashmap = {}
        for idx,word in enumerate(wordsDict):
            if word not in self.hashmap:
                self.hashmap[word] = [idx]
            else:
                self.hashmap[word].append(idx)

    def shortest(self, word1: str, word2: str) -> int:
        # word1 , word2
        dist1 = abs(min(self.hashmap[word2]) - max(self.hashmap[word1]))
        #word2, word1
        dist2 = abs(min(self.hashmap[word1]) - max(self.hashmap[word2]))

        dist3 = abs(max(self.hashmap[word2]) - max(self.hashmap[word1]))
        dist4 = abs(min(self.hashmap[word2]) - min(self.hashmap[word1]))

        return min(dist1,dist2,dist3,dist4)


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
