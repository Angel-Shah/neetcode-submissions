class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c:[] for c in range(numCourses)}

        for crs,pre in prerequisites:
            prereq[crs].append(pre)
        
        output = []
        visted,path = set(),set()

        def dfs(crs):
            if crs in path: #detected cycle
                return False
            if crs in visted:
                return True

            path.add(crs)
            visted.add(crs)

            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            path.remove(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output