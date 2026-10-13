##BUBBLE SORTING:
##def bubble_sort(l):
##    for i in range(len(l)):       #time complexity=o(n**2) bcz 2 for loops
##        for j in range(len(l)-1):
##            if l[j]>l[j+1]:
##                l[j],l[j+1]=l[j+1],l[j]
##    print(l)
##l=[3,78,93,5,1]
##bubble_sort(l)          

#SELECTION SORTING:
##l=[5,387,90,4,87]
##def selection_sort(l):        #time complexity=o(n**2) bcz 2 for loops
##    for i in range(len(l)):   
##        min_index=i
##        for j in range(i+1,len(l)):
##            if l[j]<l[min_index]:
##                min_index=j
##        l[i],l[min_index]=l[min_index],l[i]
##    print(l)
##selection_sort(l)            
    

#MERGE SORTING METHOD:
##def mergesort(l):
##    for i in range(1,len(l)):
##        key=l[i]
##        j=i-1
##        while (j>=0 and key<l[j]):
##            l[j+1]=l[j]
##            j-=1
##        l[j+1]=key
##    print(l)      
##
##l=[10,5,7,2,1,0,34,21,15,8]
##mergesort(l)

##RECURSION:
##def num(t):
##    print(t)
##    if t<10:
##        num(t+1)
##num(1)

#two recursions:
##def call(i):
##    print(i)
##    if i<5:
##        call(i+1)
##        call(i=i+i)
##
##call(1)

#MERGE SORTING:
def merge(ls):
    l=0
    m=(l+len(ls)-1)//2
    left=ls[:m]
    right=ls[m+1:len(s)]

    merge(left)
    merge(right)

    i,j,k=0,0,0
    










#ARRAY:
##from array import *
##arr=array('i',[10,20,30,40])
#print(type(arr))
#common operators:

##1.accessing
##print(arr[0])
##
##2.insert
##arr.insert(2,50)
##
##3.appending
##arr.append(100)
##
##4.removing
##arr.remove(50)
##
##print(arr)
##
##for i in arr:
##    print(i)

## 
##arr.remove(20)
##arr.insert(1,21)
##print(arr)
               
##s = {2, 4, 6, 7}
##print(s[0])
## 









