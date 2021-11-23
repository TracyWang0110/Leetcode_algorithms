class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.queue = collections.deque()
        vecs=[v1,v2]
        #遍历K哥一维向量
        for vec in vecs:
            #如果为空，就不Push进queue
            if vec:
                #对于一个List，pop(),o(1),pop(n),o(n)
                self.queue.appendleft(vec[::-1])
        print (self.queue)


    def next(self) -> int:
        # write your code here
        #队首出队
        vec = self.queue.pop()
        #list最后一个元素
        value = vec.pop()
        print(value)
        #list可能为空
        if vec:
            #非空
            self.queue.appendleft(vec)
        return value   

    def hasNext(self) -> bool:
        #不确保有下一个，是不是还有下一个
        return len(self.queue) >0 

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())

#一个行指针：上下循环移动
#一个列指针：左右移动
#如果两个指针，指向空格，寻找下个非空格

'''
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.queue = collections.deque()
        vecs=[v1,v2]
        #遍历K哥一维向量
        for vec in vecs:
            #如果为空，就不Push进queue
            if vec:
                #对于一个List，pop(),o(1),pop(n),o(n)
                self.queue.appendleft(vec[::-1])
        print (self.queue)


    def next(self) -> int:
        # write your code here
        #队首出队
        vec = self.queue.pop()
        #list最后一个元素
        value = vec.pop()
        print(value)
        #list可能为空
        if vec:
            #非空
            self.queue.appendleft(vec)
        return value   

    def hasNext(self) -> bool:
        #不确保有下一个，是不是还有下一个
        return len(self.queue) >0 

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())

'''


