class Solution:
    def isValid(self,s:str)->bool:
        my_list=['{}','()',[]]
        for i in range(len(s)-1):
            substring=s[i:i+1]
            print(substring)


obj=Solution()

# taking user input 
user_input='(){}'

# passing to the class  
obj.isValid(user_input)