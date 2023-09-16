
#errors
first_linked_list=[9,9,9,9,9,9,9]
second_linkd_list=[9,9,9,9]

def myfunction (list1,list2):
    result=[]
    count=0
    for i in range(len(list1)):
        for j in range(len(list2)):
            if i==j:
                sum=count+(list1[i]+list2[j])
                if (sum>=10):
                    sum=str(sum)
                    for i in sum:
                        if sum[0]==i:
                            ans=int(i[0])
                            count=count+ans              
                        else:
                           val=int(i)
                           result.append(val)
                else:
                    result.append(sum)
        
        
    return result





obj=myfunction(list1=first_linked_list,list2=second_linkd_list)
print(obj)

