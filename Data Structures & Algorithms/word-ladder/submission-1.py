class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        graph = defaultdict(list) # graph {pattern: [word]}
        for w in wordList:
            for c in range(len(w)):
                pattern = w[:c] + "*" + w[c+1:]
                graph[pattern].append(w)   
    
        print(f"{graph=}")
        visited = set(beginWord)
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in graph[pattern]:
                        if nei in visited:
                            continue
                        else:
                            visited.add(nei)
                            q.append(nei)
            res += 1
        return 0
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        # if endWord not in wordList:
        #     return 0
        
        # graph = defaultdict(list)
        # all_words = set(wordList)
        # all_words.add(beginWord)

        # for w in all_words:
        #     for c in range(len(w)):
        #         pattern = w[:c] + "*" + w[c+1:]
        #         graph[pattern].append(w)
        # print(f"{graph=}")

        # visit = set([beginWord])
        # q = deque([beginWord])
        # res = 1
        # while q:
        #     for i in range(len(q)):
        #         word = q.popleft()
        #         if word == endWord:
        #             return res
        #         for c in range(len(word)):
        #             pattern = word[:c] + "*" + word[c+1:]
        #             for nei in graph[pattern]:
        #                 if nei not in visit:
        #                     visit.add(nei)
        #                     q.append(nei)
        #     res += 1
        # return 0