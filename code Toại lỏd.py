f=open("danh-sách-mặt-hàng-cần-mua.txt", encoding="UTF")
bill=[]
name=[]
full=[]

for line in f:
    list_fake=[]
    l=line.split()
    name.append(l[0]) 
    moneys=int(l[1])*int(l[2]) 
    bill.append(moneys)
    list_fake.append(l[0])
    list_fake.append(moneys)
    full.append(list_fake)
print(bill)

def noibot(hangs):
    n=len(hangs)
    for i in range(n-1):
        for j in range(n-1-i):
            if hangs[j]>hangs[j+1]:
                    hangs[j],hangs[j+1]=hangs[j+1],hangs[j]
noibot(bill)
for x in bill:
     for i in range(len(full)):
          for j in range(len(full[i])):
               if full[i][j]==x:
                    print(full[i][j-1],x)
f.close()