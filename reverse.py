def helper(arr):
    l,r=0,len(arr)-1
    while(l<r):
        arr[l],arr[r]=arr[r],arr[l]
        l,r=l+1,r-1
    return arr
arr=[]
for i in range(5):
    n=int(input("Enter  a number"))
    arr.append(n)
arr=helper(arr)
s=sum(arr)
a=s//len(arr)