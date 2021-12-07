class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        #规律
        #key 是兔子回答的数字，value是这个数字出现的次数
        if answers is None:
            return 
        d = dict()
        #遍历所有兔子的回答，放进dic中
        for i in range(len(answers)):
            if answers[i] in d:
                d[answers[i]] = d[answers[i]]+1
            else:
                d[answers[i]] = 1

        #记录兔子可能最少的数量
        rabbit_num = 0

        #遍历dic,通过处理好的数据，计算出兔子的数量
        for k,v in d.items():
            #每组 可能拥有兔子的数量是K+1
            num_per_group = k+1
            #value是回答这个数字的次数
            reply_cnt =v 
            #代表了多少个不同颜色的组：整除
            number_of_group = reply_cnt//num_per_group
            #落单的兔子要分组 (余数)
            if reply_cnt % num_per_group !=0:
                number_of_group +=1
            #计算兔子总数
            rabbit_num += number_of_group*num_per_group

        return rabbit_num
