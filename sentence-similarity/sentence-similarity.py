class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
               
        #1.create a set
        #2. check word1 and word2 in an order 
        if len(sentence1) != len(sentence2):
            return False

        dic = set()
        for pf,df in similarPairs:
            dic.add((pf,df))
            dic.add((df,pf))
            #dic.add((df,df))
            #dic.add((pf,pf))
        #print (dic)
        for i in range(len(sentence1)):
            if sentence1[i] != sentence2[i]:
                if (sentence1[i], sentence2[i]) not in dic or (sentence2[i], sentence1[i]) not in dic:
                    return False
        return True