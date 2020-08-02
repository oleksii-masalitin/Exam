def avg(li):
    s=sum(i for i in li)
    return float(s)/len(li)
li1, li2, li3=[], [], []
with open('stepik6.txt', 'r') as inf, open('out6.txt', 'w') as ouf:
    while True:
        li=inf.readline().strip().split(';')
        for i in range(1,len(li)):
            li[i]=int(li[i])
        if len(li)==1:
            break
        else:
            li1.append(int(li[1]))
            li2.append(int(li[2]))
            li3.append(int(li[3]))
            ouf.write(str(avg(li[1:])))
            ouf.write('\n')
    ouf.write(str(avg(li1)))
    ouf.write(' ')
    ouf.write(str(avg(li2)))
    ouf.write(' ')
    ouf.write(str(avg(li3)))
    ouf.write(' ')