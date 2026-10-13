#BINARY SEARCH:binary search takes only sorted list,divides into two parts
##def binary_search(ls,target):
##    low=0
##    high=len(ls)-1
##    while low<=high:
##        mid=(low+high)//2
##        if ls[mid]==target:
##            return mid
##        elif ls[mid]<target:
##            low=mid+1
##        else:
##            high=mid-1
##    return -1
##
##ls=[1,2,3,4,5,6,7,8,9]
##print(binary_search(ls,9))   #time complexity is o(n)/2 ==o(log n)


#TERNARY SEARCH:ternary search takes only sorted list,divides into three parts
##def ternary_search(l,target):
##    low=0
##    high=len(l)-1
##    while(low<=high):
##        m1=low+((high-low)//3)
##        m2=high-((high-low)//3)
##        if target==l[m1]:
##            return m1
##        if target==l[m2]:
##            return m2
##        
##        if (l[m1]<target and l[m2]>target) :
##             low=m1+1
##             high=m2-1
##        elif l[m1]>target:
##             high=m1-1 
##        else:
##           low=m2+1
##    return -1
##l=[2,4,5,23,56,67,87]
##print(ternary_search(l,5))
        
#JUMP SEARCH:

import math
def jump_search(t):
    l=[0,2,3,4,5,6,7,8,9,12,14,17,19,24,28,35,38,39,42,44,46,67,69,73,77,81,89,94,96,99]
    n=len(l)
    j=int(math.sqrt(n))
    p=0
    while(j<n-1):
        p=j
        j=j*2
    if j>=n:
        j=n-1
    while (p<=j):
        if l[p]==t:
            return p
        p+=1
    return -1
print(jump_search(44))
    


#wap to count the occurence of given character in given name
##
##def ch_ct(name):
##    count=0
##    for i in name: 
##        if i in "aA":
##            count+=1
##    print(count)
##ch_ct("Akaksha")


#wap to count the occurence of each chr in given name
##d={}
##name=input("enter name:")
##for ch in name:
##    if ch not in d:
##        d[ch]=1
##    else:
##        d[ch]+=1
##print(d)











            
            
    
