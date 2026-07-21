class CharNode:
    def __init__(self):
        self.char = ''
        self.children = {}
        self.isEnding = False

class WordDictionary:
    def __init__(self):
        self.root = CharNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if (c in curr.children):
                curr = curr.children[c]
                continue
            add = CharNode()
            add.char = c
            curr.children[c] = add 
            curr = add
        curr.isEnding = True

    def search(self, word: str) -> bool:
        def dfs(jindex, root):
            cur = root
            for i in range(jindex, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if (dfs(i+1, child)):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.isEnding

        return dfs(0,self.root)
        # def recurse(i, node):
        #     # we know that c = '.'
        #     exists = False
        #     remaining = word[i:]
        #     print(remaining)
        #     for child,node in node.children.items():
        #         # we iterate through all of the children of the node we are in
        #         curr = node
        #         for i,c in enumerate(remaining):
        #             print(i)
        #             if c == '.':
        #                 return recurse(i+1,node)
        #             if c != node.char:
        #                 # go to the next child
        #                 break
        #             if(i == len(remaining)):
        #                 return curr.isEnding
        #             curr = curr.children[c]
        #     return False



        # curr = self.root
        # for i,c in enumerate(word):
        #     if c == '.':
        #         # we gotta check everything
        #         return recurse(i+1,curr)
        #     if c not in curr.children:
        #         return False
        #         break
        #     curr = curr.children[c]                
        # return curr.isEnding


        
