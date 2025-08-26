class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        queue = deque([(beginWord, 1)])
        dict_set = set(wordList)
        


        while queue:
            word, dist = queue.popleft()

            for i,w in enumerate(word):
                orig = word[i]
                for char in map(chr, range(ord('a'),ord('z')+1)) :
                    if char == orig:
                        continue
                    nextWord = word[:i] + char + word[i+1:]
                    if nextWord == endWord:
                        return dist + 1

                    if nextWord in dict_set:
                        
                        dict_set.remove(nextWord)
                        queue.append((nextWord, dist+1))

        return 0

        