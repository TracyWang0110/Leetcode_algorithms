class Solution:
    def simplifyPath(self, path: str) -> str:
        #seperate the path by '/'
        arr = path.split("/")
        print(arr)
        stack=[]
        for ch in arr:
            if ch == "..":
                if stack: #判定是不是空
                    stack.pop()
                    print (arr)
            elif ch =='.'or ch =='': 
                continue
            else:
                stack.append(ch)
        print (stack)
        
        strs=''
        if not stack:
            return '/'
        for s in stack:
            strs= strs+ '/'+s
        return strs