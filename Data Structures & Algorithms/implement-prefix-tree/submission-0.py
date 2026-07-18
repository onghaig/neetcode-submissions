class TrieNode:
    def __init__(self):
        # this is the initial node
        self.children = {}
            #  children = {letter, Node}
        self.isEnding = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        idx = 0
        currNode = self.root
        while (idx <  len(word)):
            # first see the character is in the parent node
            if (word[idx]) in currNode.children:
                currNode = currNode.children[word[idx]]
            else:
                currNode.children[word[idx]] = TrieNode()
                currNode = currNode.children[word[idx]]
            idx += 1
        currNode.isEnding = True


    def search(self, word: str) -> bool:
        cur = self.root
        currword = ""
        for c in word:
            if c in cur.children:
                currword += c
            else:
                return False
            cur = cur.children[c]
        
        return currword == word and cur.isEnding

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        currword = ""
        for c in prefix:
            if c in cur.children:
                currword += c
            else:
                return False
            cur = cur.children[c]
        return currword == prefix
        