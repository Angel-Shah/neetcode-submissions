class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0])
        l,r = 0,(rows*cols)-1
        while l <= r:
            mid = (l+r)//2
            midRow = mid//cols
            midCol = mid - (midRow*cols)
            # print(f"mid:{mid}, checking matrix[{midRow}][{midCol}]: {matrix[midRow][midCol]}")
            if matrix[midRow][midCol] > target:
                r = mid - 1
            elif matrix[midRow][midCol] < target:
                l = mid + 1
            else:
                return True
        return False