test=int(input())
for i in range(test):
    size=int(input())
    l=''
    l=input().split()
    for j in range(size):
        l[j]=int(l[j])
    m_real=sum(l)/size
    ct=0
    flag=0
    for k in l:
        ct+=1
        if ((sum(l)-k)/(size-1))==m_real:
            print(ct)
            flag=1
            break
    if flag==0:
        print("Impossible")