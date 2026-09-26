class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        
        def delta_calc(w1,w2):
            delta = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    delta += 1
            return delta
        
        graph = {w:[] for w in wordList}

        for i in range(len(wordList)-1):
            for j in range(i + 1 ,len(wordList)):
                w1 = wordList[i]
                w2 = wordList[j]
                if delta_calc(w1,w2) == 1:
                    graph[w1].append(w2)
                    graph[w2].append(w1)

        #now that we have built the graph, we do BFS startWord to find the endWord

        q = deque([beginWord])
        min_words = 1
        visited = set([beginWord])
        while q:
            print(f"iteration {min_words}: q look like => {q}")
            for _ in range(len(q)):
                curr_word = q.popleft()
                if curr_word == endWord:
                    return min_words
                for nei in graph[curr_word]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            min_words += 1

        return 0