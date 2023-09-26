#if the list is [1,2,3] then you need to add 1 the n the result will be [1,2,4]

def plusOne(mylist):
    val=[]
    num=0
    for i in mylist:
        num=num *10+ i
    
    num=num+1
    
    while num>0:
        digit=num%10
        val.insert(0,digit)
        num=num//10
    
    return val


mylist=[1,2,3]

result=plusOne(mylist)
print(result)
