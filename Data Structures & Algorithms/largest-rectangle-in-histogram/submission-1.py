class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largestRect = 0
        stack = []
        for i,h in enumerate(heights):
            if not stack or stack[-1][1] < h:
                stack.append((i,h))
            else:

                popIdx,popHeight = stack.pop()
                while stack and stack[-1][1] > h:
                    popIdx,popHeight = stack.pop()
                    largestRect = max(largestRect,popHeight*(i-popIdx))
                largestRect = max(largestRect,popHeight*(i-popIdx))
                stack.append((popIdx,h))
            # print(stack)
            # print(largestRect)

        for s in stack:
            largestRect = max(largestRect,s[1]*(len(heights)-s[0]))

        return largestRect

                    