from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for row in range(n):
            row_hash = set()
            for col in range(n):
                val = board[row][col]
                if val == '.':
                    continue
                if val in row_hash:
                    return False
                row_hash.add(val)

        for col in range(n):
            col_set = set()
            for row in range(n):
                val = board[row][col]
                if val == '.':
                    continue
                if val in col_set:
                    return False
                col_set.add(val)

        grid_hash = defaultdict(set)
        for row in range(n):
            i = row // 3
            for col in range(n):
                val = board[row][col]
                if val == '.':
                    continue
                j = col // 3
                subbox = i * 3 + j
                if val in grid_hash[subbox]:
                    return False
                grid_hash[subbox].add(val)
        return True