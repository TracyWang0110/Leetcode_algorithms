class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        if len(s)!=len(goal): 
            return False
        #a和b相等时的一些边界情况
        if s==goal and len(set(s))==len(s): #ab, ab
            return False 
        if s==goal and len(set(s))<len(s): #aa, aa, aba, aba
            return True
        #遍历A和B
        c =""
        for i in range(len(s)):
            if s[i]!= goal[i]:
                c += s[i]
                c += goal[i]
        if len(c) == 4 and c == c[::-1]: #是不是对称的
            return True
        return False     
            