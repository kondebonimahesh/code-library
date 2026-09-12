# merge sort by me crmy  
def merge(ar,low,mid,high) :
    n=len(ar)  
    i,j=low,mid+1
    k,temp=low,[0]*n
    while i<=mid and j<=high :
        if ar[i]<=ar[j] :
            temp[k]=ar[i]
            i+=1 
        else :
            temp[k]=ar[j]
            j+=1 
        k+=1
    while i<=mid :
        temp[k]=ar[i]
        k+=1
        i+=1  
    while j<=high :
        temp[k]=ar[j]
        k+=1 
        j+=1 
    for g in range(low,high+1) :
        ar[g]=temp[g]
    
def div(ar,low,high) :
    if low>=high :
        return 
    mid=low+(high-low)//2 
    div(ar,low,mid)
    div(ar,mid+1,high) 
    merge(ar,low,mid,high) 


div(ar,0,len(ar)-1) 

print(ar)
