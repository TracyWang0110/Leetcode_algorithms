class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        #Split both strings by dot character into two arrays.
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        n1 = len(nums1)
        n2 = len(nums2)
        
        #compare versions
        #leading zero will be removed after using int function
        #add 0 for shorter one till they have mathced length
        
        for i in range(max(n1,n2)):
            if i < n1:
                i1 = int(nums1[i])
            else:
                i1 = 0
                         
            if i < n2:
                i2 = int(nums2[i])
            else:
                i2 = 0
                
            if i1>i2:
                return 1
            elif i1<i2:
                return -1
        #versions are equal
        return 0