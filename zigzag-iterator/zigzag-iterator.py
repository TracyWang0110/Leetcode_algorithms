class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.row_index =0
        self.col_index =0
        self.vecs = [v1,v2]
        self.non_empty_vec_cnt = len(self.vecs)
        #遍历每一行
        for i in range(len(self.vecs)):
            if len(self.vecs[i]) ==0:
                self.non_empty_vec_cnt -= 1
        #非空行遍历，是不是还有下一个元素可以取遍历

    def next(self) -> int:
        #跳过所有已经终结的行，直周到下一个可以返回的行
        while self.col_index >=len(self.vecs[self.row_index]):
            self.row_index +=1
            #如果已经到了末行，行回到0,列加1
            if self.row_index == len(self.vecs):
                #回到row_index 0 
                self.row_index = 0
                self.col_index +=1
            
        
        
        value = self.vecs[self.row_index][self.col_index]
        #如果当前行已经遍历完，deactivate 
        if self.col_index == len(self.vecs[self.row_index])-1:
            self.non_empty_vec_cnt -=1
        
        #行+1
        self.row_index  += 1
        
        #如果已经到了末行，行回到0，列加1
        if self.row_index == len(self.vecs):
            self.row_index = 0
            self.col_index +=1
            
        return value
        


    def hasNext(self) -> bool:
        #不确保有下一个，是不是还有下一个
        return self.non_empty_vec_cnt >0 
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())

#一个行指针：上下循环移动
#一个列指针：左右移动
#如果两个指针，指向空格，寻找下个非空格


