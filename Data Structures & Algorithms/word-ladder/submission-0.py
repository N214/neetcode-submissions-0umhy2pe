class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        graph = defaultdict(list)
        all_words = set(wordList)
        all_words.add(beginWord)

        for w in all_words:
            for c in range(len(w)):
                pattern = w[:c] + "*" + w[c+1:]
                graph[pattern].append(w)
        print(f"{graph=}")

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for c in range(len(word)):
                    pattern = word[:c] + "*" + word[c+1:]
                    for nei in graph[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            res += 1
        return 0