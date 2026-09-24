class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        stack = []
        # stack.append([float('inf'),len(heights)-1])

        result = []

        for i in range(len(heights)-1,-1,-1):
            if not stack:
                result.append(0)
            else:
                if heights[i] < stack[-1]:
                    result.append(1)
                else:
                    pop_count = 0
                    while stack and heights[i] > stack[-1]:
                        pop_count += 1
                        stack.pop(-1)
                    if stack:
                        pop_count += 1
                    result.append(pop_count)
            
            stack.append(heights[i])
        
        return result[::-1]