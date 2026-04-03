class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        if len(nums2) < len(nums1):
            A,B = B,A
        total = len(A)+len(B)
        halfway = (total)//2

        l,r = 0, len(A)-1
        
        while True:
            a_idx = (l+r)//2
            b_idx = halfway - (a_idx + 1) - 1 #addtional -1 due to 0-index in b 

            A_left = A[a_idx] if a_idx >= 0 else float('-inf')
            A_right = A[a_idx+1] if (a_idx + 1) < len(A) else float('inf')
            B_left = B[b_idx] if b_idx >= 0 else float('-inf')
            B_right = B[b_idx+1] if (b_idx +1) < len(B) else float('inf')

            if A_left <= B_right and B_left <= A_right: #found partition, return
                if total%2 ==0:
                    return (max(A_left,B_left) + min(A_right,B_right))/2
                else:
                    return min(A_right,B_right)
            elif A_left > B_right:
                r = a_idx - 1 
            else:
                l = a_idx + 1