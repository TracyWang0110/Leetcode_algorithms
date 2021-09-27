class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #without changing the order, so it cannot be sorted.
        sub = [nums[0]]
        
        for num in nums[1:]:
            #keep adding the element if num is larger than the last element
            if num > sub[-1]:
                sub.append(num)
            #if not, scan the the sub list,till find the the element position that current number is samller or equal than that element
            else:            
                i = 0 #find the index
                while num > sub[i]:
                    i=i+1
                sub[i] = num
        return len(sub)
                
                
        
        
            