from math import floor 
integer,count=map(int,input().split())
while integer>0 and count>0:
    res=integer%10
    if(res==0):
        count-=1
        integer=floor(integer/10)
    else:
        if(count>=res+1):
            count-=res+1
            integer=floor(integer/10)
        else:
            integer=integer-count
            count=0
print(integer)
