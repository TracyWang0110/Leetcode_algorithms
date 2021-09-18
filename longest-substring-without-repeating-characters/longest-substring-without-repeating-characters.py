class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #1.use hash table to store the last index
        #2.keep track the valid starting point
           #when there is a match, update the starting point to the current one
        dic={}
        left = 0
        right = 0
        ans = 0 #tracking the lengh
        while (left<len(s) and right<len(s)):
            if s[right] in dic:
                left=max(left, dic[s[right]]+1)
            #update index to right in hashtable 
            dic[s[right]] = right
            ans = max(ans,right-left+1 )
            right = right +1
        return ans