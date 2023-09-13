# strs=["flower",'flow','flight']
# strs=['ab','abcd','cd']
strs=['cir','car']

ans=""
v=sorted(strs)
first=v[0]
first=(first[:2])

# print(first)
count=0
for s in v:
    # print(s)
    if s[:2] == first or s[:1]==first:
        #  print(s[:2])
         count+=1

# print(count)
if len(v)== count:
     print(first,"this ")  

else:
     print("empty")

last=v[-1]
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