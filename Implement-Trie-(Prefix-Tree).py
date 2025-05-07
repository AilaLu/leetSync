class TrieNode:
    def __init__(self):
        self.children = {} #the 26 alphabets, with a hashmap
        self.endOfWord = False # default as false, if it's an end of a word, set it to true



class Trie:

    def __init__(self):
        self.root = TrieNode() #the trie tree is indicated by the root node.
        

    def insert(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode() #create a new node 
            cur = cur.children[char] #point to the next node
            
        cur.endOfWord = True #after inserting all, set the end of the word node to be true


    def search(self, word: str) -> bool:
        cur = self.root

        for char in word:
            if char not in cur.children: return False #it's not a word in the trie tree
            cur = cur.children[char] #point to the next node
         
        return cur.endOfWord 
        # return True if cur.endOfWord == True else False
        

    def startsWith(self, prefix: str) -> bool:
        #the difference between search and startsWith is that search has the endOfWord == True
        cur = self.root

        for char in prefix:
            if char not in cur.children: return False
            cur = cur.children[char] #point to the next node

        return True

        






# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)