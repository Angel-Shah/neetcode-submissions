class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        hashmap = {}
        nHash = {}
        wordList.append(beginWord)
        foundEndWord = False
        for word in wordList:
            hashmap[word] = set()
            if word == endWord:
                foundEndWord = True
            for i in range(len(word)):
                curr = word[:i]+"*"+word[i+1:]
                hashmap[word].add(word[:i]+"*"+word[i+1:])
                if curr in nHash:
                    nHash[curr].append(word)
                else:
                    nHash[curr] = []
                    nHash[curr].append(word)
        
        if not foundEndWord:
            return 0

        # print(nHash)  
        adjList = {}

        for pattern,wrds in nHash.items():
            if len(wrds) > 1:
                for i in range(len(wrds)):
                    if wrds[i] not in adjList:
                        adjList[wrds[i]] = wrds[:i]+wrds[i+1:]
                    else:
                        adjList[wrds[i]]+=(wrds[:i]+wrds[i+1:])
        print(adjList)   

        # for key in hashmap:
        #     adjList[key] = []
        #     for k2 in hashmap:
        #         if key == k2:
        #             continue
        #         overlap = hashmap[key] & hashmap[k2]
        #         if overlap:
        #             adjList[key].append(k2)
        
        # now do BFS from beginWord and branch out until we reach endWord
        q = deque()
        q.append(beginWord)
        visited = set()
        depth = 0
        while q:
            for i in range(len(q)):
                wrd = q.popleft()
                if wrd == endWord:
                    return depth+1
                visited.add(wrd)
                for nei in adjList[wrd]:
                    if nei not in visited:
                        q.append(nei)
            depth +=1

        return 0