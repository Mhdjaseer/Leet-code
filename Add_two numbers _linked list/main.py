

first_linked_list=[2,4,5]
second_linkd_list=[5,6,4]

def myfunction (list1,list2):
    result=[]
    for i in range(len(list1)):
        for j in range(len(list2)):
            count=0
            if i==j:
                sum=count+(list1[i]+list2[j])
                result.append(sum)
                if (sum>=10):
                    sum=str(sum)
                    for i in reversed(sum):
                        if i == i[0]:
                            result.append(i[0])
                        else:
                            count=i[1]
    return result





obj=myfunction(list1=first_linked_list,list2=second_linkd_list)
print(obj)

