class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rows = cols = n
        usedDlDiag = set() #do row+col
        usedDrDiag = set()# do row-col
        usedRows = set()
        usedCols = set()
        
        queens = n
        answer = []
        currPart = []

        def dfs(r):
            if r>= rows:
                answer.append(currPart.copy())
                return
            
            for c in range(cols):
            
                if (r not in usedRows and
                    c not in usedCols and
                    (r-c) not in usedDrDiag and 
                    (r+c) not in usedDlDiag
                ):
                    usedRows.add(r)
                    usedCols.add(c)
                    usedDlDiag.add(r+c)
                    usedDrDiag.add(r-c)

                    string = "." * n
                    newStr = string[:c]+'Q'+string[c+1:]
                    currPart.append(newStr[:])

                    dfs(r+1)

                    currPart.pop()

                    usedRows.remove(r)
                    usedCols.remove(c)
                    usedDlDiag.remove(r+c)
                    usedDrDiag.remove(r-c)
            
        dfs(0)

        return answer


            

