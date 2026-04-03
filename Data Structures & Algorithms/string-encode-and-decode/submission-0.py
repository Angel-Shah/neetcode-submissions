class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        # print(res)
        return res
        

    def decode(self, s: str) -> List[str]:
        res = []
        #getting the length
        length = ""
        idx = 0
        while idx < len(s):
            if s[idx] != '#':
                length += s[idx]
                idx +=1
                continue
            # if it reaches here it means that we have reached a '#'
            res.append(s[idx+1:idx+int(length)+1])
            idx += (int(length)+1)
            length = ""
        return res
            
        
            
        
