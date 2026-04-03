class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

    def addFolder(self,path):
        dirs = path.split('/')

        curr = self
        for d in dirs:
            if d not in {"","/"}:
                if d not in curr.children:
                    curr.children[d] = TrieNode()
                curr = curr.children[d]
        curr.isEnd = True

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode()
        #populating tree with all folder paths
        for f in folder:
            root.addFolder(f)
        
        # running dfs and returning early when end of a folder path is found
        result = []
        def dfs(node, currWord, result):
            if node.isEnd:
                result.append(currWord)
            else:
                for d,child in node.children.items():
                    dfs(child, currWord + "/" + d, result)

        dfs(root,"",result)
        return result