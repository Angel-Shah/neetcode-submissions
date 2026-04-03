class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedPostions = sorted(enumerate(position), key=lambda x: x[1])
        ans = 0
        stepsToTarget = []
        for idx,pos in sortedPostions:
            stepsToTarget.append((target-pos)/speed[idx])
        # print(stepsToTarget)

        while stepsToTarget:
            curr = stepsToTarget.pop()
            ans += 1
            while stepsToTarget and stepsToTarget[-1] <= curr:
                stepsToTarget.pop() 
        return ans
