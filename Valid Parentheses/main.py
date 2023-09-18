
#error not compleated 
class Solution:
    def isValid(self,s:str)->bool:
        my_list=['{}','()',[]]
        for i in range(len(s)):
            if i%2==0:
                print(s[i])



obj=Solution()

# taking user input 
user_input='(){}'

# passing to the class  
obj.isValid(user_input)