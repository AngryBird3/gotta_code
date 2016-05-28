class Solution:
    def __init__(self):
        self.trie = {}
    def addWords(self, dict_words):
        for word in dict_words:
            node = self.trie
            for w in word:
                if w not in node:
                    node[w] = {}
                node = node[w]
            node['_end_'] = True


    def startsWith(self, prefix):
        node = self.trie
        for w in prefix:
            if w not in node:
                return list()
            node = node[w]
        res = list()
        self.dfs(node, prefix, res)
        return res

    def dfs(self, node, word, res):
        if '_end_' in node:
            res.append(word)
            return
        for w in node:
            self.dfs(node[w], word + w, res)

s = Solution()
words = ["trie", "tree", "root", "tram", "tea", "road"]
s.addWords(words)
print s.startsWith("tr")
