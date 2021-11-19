class Solution:
    def fib(self, n: int) -> int:
        '''
        if n==1:
            return 0
        if n==2:
            return 1
        return self.fib(n-1)+self.fib(n-2)
    
        #2n次方
        '''
        if n<=1:
            return n
        
        first = 0
        second = 1
        third = 0
        i = 2
        
        while i <= n:
            third = first+second
            first = second
            second = third
            i +=1
        return third 
            