class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_dic = {el:0 for el in s}

        t_dic = {el:0 for el in t}

        
        for i in range(len(s)):
            if s[i] in s_dic:
                s_dic[s[i]] +=1
                #print(s_dic)
                
        for i in range(len(t)):
            if t[i] in t_dic:
                t_dic[t[i]] +=1
        print(t_dic)
        
        return s_dic == t_dic



        