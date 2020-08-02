def avg(li):
    s=sum(i for i in li)
    return float(s)/len(li)
li1, li2, li3=[], [], []
while True:
    li=input().strip().split(';')
    for i in range(1,len(li)):
        li[i]=int(li[i])
    if li=='':
        break
    else:
        li1.append(int(li[1]))
        li2.append(int(li[2]))
        li3.append(int(li[3]))
        print(avg(li[1:]))

#with open('spepik4.txt', 'r') as inf, open('out4.txt', 'w') as ouf:
