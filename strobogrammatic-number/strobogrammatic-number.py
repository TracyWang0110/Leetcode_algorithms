class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        #hashtable:dictionary 
        #if in the table, replace it with corresponding item in dictionary 
        # and then see num and rotated num are same
        
        rotated_digits = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        
        rotated_num = []
        
        for char in num[::-1]:
            if char not in rotated_digits:
                return False 
            if char in rotated_digits:
                rotated_num.append(rotated_digits[char])
                    
                
        return num == "".join(rotated_num)