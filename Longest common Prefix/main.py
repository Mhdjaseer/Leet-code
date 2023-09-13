# strs=["flower",'flow','flight']
# strs=['ab','abcd','cd']
strs=['cir','car']

class Solution:
    def longestCommonPrefix(self,v):
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 
obj=Solution()
result=obj.longestCommonPrefix(strs)
print(result)
#     if s[:2] == first:
#          print(s[:2])
#          count+=1


# while count < len(v):
#     current_str = v[count]
#     print(current_str,"no repeat")
#     for i in range(len(current_str)):
#         print(current_str[i])
#     count += 1




# print(count)
# if len(v)== count:
#      print(first,"this ")  

# else:
#      print("empty")

# last=v[-1]
# print(first)
# print(last)
# def prefix(first,last):
#     for i in range(min(len(first),len(last))):
#         if (first [i]!=last[i]):
#             return ans
#         ans+=first[i]

#         return ans

# obj=prefix(first=first,last=last)
# print(obj)