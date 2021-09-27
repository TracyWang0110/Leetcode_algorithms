class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #sort method 
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
        
        
        #binary search 
        
        #left and right represent the range of vaules of the target
        left = 1
        right = len(nums) -1
        
        while left<=righ:
            #find the mid point 
            cur = (left+right)//2
            count = 0
        #count how many numbers are less than or equal to 'cur'
        for num in nums:
            count = count+1

        if count > curr:
            right = cur-1
        else:
            left = cur + 1
        return right
            
            
        
            