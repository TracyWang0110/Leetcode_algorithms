class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #binary search problems
        if len(nums) == 0: return [-1, -1]
        start, end = -1,-1
        
        left = 0
        right = len(nums)-1
        
        #binary search left
        while left <= right:
            mid = (left+right)//2
            if nums[mid]>=target:
                right = mid-1
            else:
                left = mid +1 
        if left <len(nums) and nums[left]==target: 
            start = left
            
        #reset left and right 
        left =0
        right =len(nums)-1
        while left <= right:
            mid =(left+right)//2
            if nums[mid] <= target:
                left = mid+1
            else:
                right = mid-1
                
        if nums[right]==target:
            end = right
                        
        return [start,end]
            

            
        