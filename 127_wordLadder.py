import collections
from typing import List

class Solution:
    def getPatterns(self, word):
        p = []
        for j in range(len(word)):
            p.append(word[:j] + "*" + word[j + 1:])
        return p

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for pattern in self.getPatterns(word):
                nei[pattern].append(word)

        visit = set([beginWord])
        q = collections.deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for pattern in self.getPatterns(word):
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0

#########################
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = collections.deque([beginWord])

        pattern_word = collections.defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i + 1:]
                pattern_word[pattern].append(w)

        res = 1
        visited = set(beginWord)
        while q:
            for i in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return res
                visited.add(w)
                for i in range(len(w)):
                    pattern = w[:i] + "*" + w[i + 1:]
                    for next_w in pattern_word[pattern]:
                        if next_w not in visited:
                            q.append(next_w)
            res += 1
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i + 1:]
                adj[pattern].append(w)

        q = deque([beginWord])
        length = 1
        visit = set()
        while q:
            for i in range(len(q)):
                w = q.popleft()
                visit.add(w)
                if w == endWord:
                    return length
                for i in range(len(w)):
                    pattern = w[:i] + "*" + w[i + 1:]
                    for nei in adj[pattern]:
                        if nei not in visit:
                            q.append(nei)
            length += 1
        return 0


"""
127. Word Ladder
Hard

9061

1721

Add to List

Share
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to 
endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
Accepted
839,267
Submissions
2,302,991
"""