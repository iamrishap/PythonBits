"""
Given two words A and B, and a dictionary, C, find the length of shortest transformation sequence from A to B, such that:

You must change exactly one character in every transformation.
Each intermediate word must exist in the dictionary.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.


Input Format:

The first argument of input contains a string, A.
The second argument of input contains a string, B.
The third argument of input contains an array of strings, C.
Output Format:

Return an integer representing the minimum number of steps required to change string A to string B.
Constraints:

1 <= length(A), length(B), length(C[i]) <= 25
1 <= length(C) <= 5e3
Example :

Input 1:
    A = "hit"
    B = "cog"
    C = ["hot", "dot", "dog", "lot", "log", "cog"]

Output 1:
    5

Explanation 1:
    "hit" -> "hot" -> "dot" -> "dog" -> "cog"
"""


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not wordList:
            return 0

        n = len(wordList)
        begin_flag = False
        List = set()
        for word in wordList:
            List.add(word)

        if endWord not in List:
            return 0
        if beginWord in List:
            begin_flag = True

        graph = {}

        if not begin_flag:
            graph[beginWord] = []

            for i in range(n):
                if self.dist_one(beginWord, wordList[i]):
                    graph[beginWord].append(wordList[i])
                    graph[wordList[i]] = [beginWord]

        for i in range(n):
            if wordList[i] not in graph:
                graph[wordList[i]] = []
            word = wordList[i]
            for j in range(len(word)):
                for num in range(ord('a'), ord('z') + 1):
                    s = word[:j] + chr(num) + word[j + 1:]
                    if s in List:
                        graph[word].append(s)

        res = self.bfs(graph, beginWord, endWord) + 1

        return res

    def dist_one(self, string1, string2):
        count = 0
        n = len(string1)
        for i in range(n):
            if string1[i] != string2[i]:
                count += 1
            if count > 1:
                return False
        return True

    def bfs(self, graph, beginword, endword):
        visited = set()
        queue = []
        queue.append([beginword, 0])
        visited.add(beginword)

        while queue:
            [string, count] = queue.pop(0)
            if string == endword:
                found = True
                return count
            for item in graph[string]:
                if item not in visited:
                    queue.append([item, count + 1])
                    visited.add(item)
        return -1


A = "hit"
B = "cog"
C = ["hot", "dot", "dog", "lot", "log", "cog"]

s = Solution()
print(s.ladderLength(A, B, C))
