class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first_idx,second_idx = 0,0
        result = []
        while first_idx < len(firstList) and second_idx < len(secondList):

            f_start,f_end = firstList[first_idx][0],firstList[first_idx][1]
            s_start,s_end = secondList[second_idx][0],secondList[second_idx][1]

            start = max(f_start,s_start)
            end = min(f_end,s_end)

            if start <= end:
                result.append([start,end])
            
            if f_end < s_end:
                first_idx += 1
            else:
                second_idx += 1
        return result