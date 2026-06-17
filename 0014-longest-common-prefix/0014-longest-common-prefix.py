class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        trie = Trie()
        for s in strs:
            trie.insert(s)
        
        prefix = []
        curr = trie.root
        while (len(curr.children)==1 and not curr.last):
            ch = next(iter(curr.children))
            prefix.append(ch)
            curr = curr.children[ch]
        return ''.join(prefix)

        

class TrieNode:
    def __init__(self):
        self.children = {}
        self.last = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        curr = self.root
        #print('INSIDE')
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr=curr.children[ch]
        curr.last = True

    

