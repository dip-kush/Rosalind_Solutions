f=open('rosalind_trie.txt')
l=f.read().strip()
l=l.split('\n')


NodeCount=1
class Node():
    pass

def traverse(t):
    global NodeCount
    for letter in t.children:
        print t.value,t.children[letter].value,letter 
        traverse(t.children[letter])  
        

class TrieNode:
    def __init__(self):
        global NodeCount
        self.value=NodeCount
        self.children = {}
        NodeCount += 1

    def insert( self, word ):
        node = self
        for letter in word:
            if letter not in node.children: 
                node.children[letter] = TrieNode()

            node = node.children[letter]


trie=TrieNode()

for item in l:
    trie.insert(item)  


traverse(trie)
     
