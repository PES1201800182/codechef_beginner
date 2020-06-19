def give_index(time_stamp):
    nextind=0
    res={}
    for t,check,_ in time_stamp:
        if check!=2 and t not in res:
            res[t]=nextind
            nextind+=1
    return res
def add_sum(tree,index,value):
    while index<len(tree):
        tree[index]+=value
        index+=index&(-index)
def give_sum(tree,index):
    res=0
    while index>0:
        res+=tree[index]
        index-=index&-index
    return res

no_of_shows=int(input())
time_stamp=[]
START,CHECK,END=0,1,2
for i in range(no_of_shows):
    start,end=map(int,input().split())
    time_stamp.append((start,START,None))
    time_stamp.append((end,END,start))
total_queries=int(input())
for i in range(total_queries):
    for j in map(int,input().split()[1:]):
        time_stamp.append((j,CHECK,i))
time_stamp=sorted(time_stamp)
indexed=give_index(time_stamp)
tree=[0]*(len(indexed)+1)
final_result=[0]*total_queries
prev_result=[None]*total_queries
for i in time_stamp:
    start,value,end=i
    if(value==START):
        add_sum(tree,indexed[start]+1,1)
    elif(value==END):
        add_sum(tree,indexed[end]+1,-1)
    else:
        query_no=end
        final_result[query_no]+=give_sum(tree,indexed[start]+1)
        if(prev_result[query_no]!=None):
            final_result[query_no]-=give_sum(tree,prev_result[query_no])
        prev_result[query_no]=indexed[start]+1

for i in final_result:
    print(i)
