class TrieNode:
    def __init__(self):
        self.children = {}
        self.isFile = False
        self.content = ""

    def addDir(self,path):
        dirs = path.split('/')
        curr = self
        for d in dirs:
            if d not in curr.children:
                curr.children[d] = TrieNode()
            curr = curr.children[d]
        return curr
class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        res = []
        objs = path.split('/')
        curr = self.root
        for obj in objs:
            if obj in curr.children:
                curr = curr.children[obj]
        if curr.isFile:
            return [objs[-1]]
        else:
            for key,val in curr.children.items():
                res.append(key)
            return sorted(res)

    def mkdir(self, path: str) -> None:
        self.root.addDir(path)
        # curr = self.root
        # dirs = path.split('/')
        # for d in dirs:
        #     if d in curr.children:
        #         curr = curr.children[d]
        #     else:
        #         curr.children[d] = TrieNode()

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.root
        dirs = filePath.split('/')
        for d in dirs:
            if d not in curr.children:
                curr.children[d] = TrieNode()
            curr = curr.children[d]
        curr.isFile = True
        curr.content += content

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.root
        dirs = filePath.split('/')
        for d in dirs:
            if d not in curr.children:
                return ""
            curr = curr.children[d]
        return curr.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
