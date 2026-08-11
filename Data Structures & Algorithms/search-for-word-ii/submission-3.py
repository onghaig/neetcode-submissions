class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # this is going to be a dfs problem
        # graph problem + trie problem
        tree = PrefixTree()
        for word in words:
            tree.insert(word)
        visited = set()
        ROWS = len(board)
        COLS = len(board[0])
        res = []
        # char: 
        def dfs(position, currNode, currWord):
            r,c = position
            if (r >= ROWS or c >= COLS or r < 0 or c < 0):
                return 
            if (position in visited):
                return 
            if (board[r][c] in currNode.children):
                currNode = currNode.children[board[r][c]]
                currWord += board[r][c]
                visited.add((r,c))
                if (currNode.isEnding):
                    res.append(currWord)
                    currNode.isEnding = False
            else:
                return
            dfs((r,c +1), currNode, currWord)
            dfs((r,c - 1), currNode, currWord)
            dfs((r + 1,c), currNode, currWord)
            dfs((r - 1,c), currNode, currWord)
            visited.remove((r,c))
    
                # how can we implement visited? would you have to have a table and for each element in the table,
            # we have its own set for the word
        # what should dfs return? maybe nothing, also how can i track the current word we are on
        for x in range(ROWS):
            for y in range(COLS):
                tup = (x,y)
                dfs(tup, tree.root, "")
        return res
        


    
class TrieNode:
    def __init__(self):
        self.children = {}
        # {a : trieNode()}
        self.isEnding = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        # root node -> x num of children,
        # each child node looks like root
        currNode = self.root
        for char in word:
            if (char in currNode.children):
                currNode = currNode.children[char]
            else:
                currNode.children[char] = TrieNode()
                currNode = currNode.children[char]
        currNode.isEnding = True
    

        
