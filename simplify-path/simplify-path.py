class Solution:
    def simplifyPath(self, path: str) -> str:
        #seperate the path by '/'
        arr = path.split("/")
        print(arr)
        stack=[]
        #会遇到什么呢，会遇到.,空串，，..
        for ch in arr:
            #返回上级目录
            if ch == "..":
                if stack: #判定是不是空，在写Pop之前就一定要判定
                    stack.pop()
                    print (arr)
            elif ch =='.'or ch =='': 
                continue
            else:
                stack.append(ch)
        print (stack)
        
        '''
        strs=''
        #如果栈是空的，返回跟目录
        if not stack:
            return '/'
        for s in stack:
            strs= strs+ '/'+s
        return strs
        '''
        return '/'+'/'.join(stack)
        