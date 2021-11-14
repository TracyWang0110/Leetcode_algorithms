class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #slicing windown 
        #建立start pointer 遍历
        #每次查start to start+len(p)
        '''
        res=[]
        for start in range(len(s)-len(p)+1):
            #print(start)
            t = ''.join(sorted(s[start:start+len(p)]))
                               
            if t == ''.join(sorted(p)):
                res.append(start)
        return res
        #time exceed limits
        '''      
        if len(s) < len(p):
            return []
        #存放的s，p的26个字母
        p_count = [0]*26
        s_count =[0]*26
        
        for ch in p:
            p_count[(ord(ch))-ord('a')] +=1
            res=[]
        for i in range(len(s)):
        #每出现一个字母更新字母的次数
            s_count[ord(s[i])-ord('a')] +=1
        #开始移动窗口
            if i>=len(p):
                s_count[ord(s[i-len(p)])-ord('a')] -=1
            if p_count == s_count:
                res.append(i-len(p)+1)
        return res
        
        
            