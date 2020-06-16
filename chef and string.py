a=int(input())
i=0
while(i<a):
    arr=input()
    length=len(arr)
    prev=arr[0]
    used=0
    count=0
    for i in range(1,length):
        if(used!=0&&prev!=arr[i]):
            count++
            used=1
        else:
            used=0
        prev=arr[i]
    print(count)
