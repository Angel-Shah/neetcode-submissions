class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        hashmap = {}
        wordList.append(beginWord)
        for word in wordList:
            hashmap[word] = set()
            for i in range(len(word)):
                hashmap[word].add(word[:i]+"*"+word[i+1:])
        
        if endWord not in hashmap:
            return 0

        adjList = {}

        for key in hashmap:
            adjList[key] = []
            for k2 in hashmap:
                if key == k2:
                    continue
                overlap = hashmap[key] & hashmap[k2]
                if overlap:
                    adjList[key].append(k2)
        
        print(adjList)
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