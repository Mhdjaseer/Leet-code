
#error not compleated 
class Solution:
    def isValid(self,s:str)->bool:
        my_list=['{}','()',[]]
        for i in range(len(s)):
            substring=s[i:i+1]
            for j in range(len(my_list)):
                if substring and (substring)==my_list[i]:
                    print("hi")


obj=Solution()

# taking user input 
user_input='(){}'

# passing to the class  
obj.isValid(user_input)