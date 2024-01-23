int(input("Enter how many you want to input:\n"))
arr=list(map(int,input("Enter array elements:\n").split()))

search=int(input("enter search num:"))
n=len(sorted(arr))
l,h=0,n-1
result=-1

while(l<=h):
    mid=(l+h)//2
    if(arr[mid]==search):
        result=mid
        break
    elif(arr[mid]<search):
        l=mid+1
    else:
        h=mid-1
if(result!=-1):
    print("{} item found at position {}".format(search,result))
else:
    print("{} not found".fotmat(search))
    