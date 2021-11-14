class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #建一个Hash table
        #把这个hash tabel的key都找出来
        dic={}
        for s in strs:
            join_s = ''.join(sorted(s))
            print(join_s)
            
            if join_s not in dic:
                #如果找不到第二个相同的Key
                dic[join_s] = [] #instead of count 0, return a empty list
            #第一个key都加入dic
            dic[join_s].append(s)
        return dic.values()
        

                