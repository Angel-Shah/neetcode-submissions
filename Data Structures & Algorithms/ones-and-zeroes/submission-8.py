class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        cache = {}

        def dfs(i , curr_ones, curr_zeros):
            if i == len(strs):
                return 0
            if (i,curr_ones,curr_zeros) in cache:
                return cache[(i,curr_ones,curr_zeros)]
         

            new_ones = strs[i].count('1')
            new_zeros = strs[i].count('0')

            #not included
            cache[(i,curr_ones,curr_zeros)] = dfs(i+1,curr_ones,curr_zeros)


            #if included
            if (curr_ones + new_ones) <= n and (curr_zeros + new_zeros) <= m:
                cache[(i,curr_ones,curr_zeros)] = max(cache[(i,curr_ones,curr_zeros)], dfs(i+1,curr_ones + new_ones,curr_zeros + new_zeros) + 1)

            return cache[(i,curr_ones,curr_zeros)]
                
        
        

        return dfs(0,0,0)
