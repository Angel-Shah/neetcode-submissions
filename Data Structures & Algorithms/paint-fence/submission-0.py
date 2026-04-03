class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k
        
        same = k
        different = k * (k-1)
        if n ==2:
            return same+different
        
        prev_same,prev_different = same, different

        for _ in range(3,n+1):
            same = prev_different
            different = (prev_same + prev_different)*(k-1)

            prev_same,prev_different = same, different

        return same+different
