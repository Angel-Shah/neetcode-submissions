class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        maxVal = float('-inf')

        for i in range(len(arr)-1,-1,-1):
            if i == len(arr)-1:
                maxVal = arr[i]
                arr[i] = -1
                continue
            tmp = arr[i]
            arr[i] = maxVal
            maxVal = max(maxVal,tmp)
        
        return arr