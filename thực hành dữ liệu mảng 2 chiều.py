# nhập dữ liệu
names=[]
marks=[]
n=int(input("nhập số lượng học sinh:"))
for i in range(n):
    name=input("nhập tên học sinh thứ"+str(i+1)+": ")
    names.append(name)
    mark=input("nhập điểm học sinh:")
    point=[int(x) for x in mark.split()]
    marks.append(point)
# thống kê dữ liệu
avg=[]
max=0
ten=0
min=marks[0][0]
for i in range(n):
    tb=0
    for j in range(len(marks[i])):
        tb+=marks[i][j]
        if marks[i][j]<min:
            min=marks[i][j]
    tb=tb/len(marks[i])
    avg.append(tb)
    if tb>max:
        max=tb
        ten=names[i]
    print("điểm trung bình của học sinh", names[i], "là",tb)
print("học sinh có điểm trung bình cao nhất là:",ten ,"với ", max,"điểm")
print("điểm thấp nhất trong các đầu diểm là:",min)
# tra cứu điểm học sinh và tìm điểm của học sinh cụ thể
def find(num):
    if num<=n:
        print("đầu điểm của học sinh thứ ",num,"là",marks[num-1])
    else:
        print("vui lòng nhập đúng số thứ tự")
def finds(nums,th):
    if nums<=n:
        if th<=len(marks[nums-1]):
            print("cột điểm tra cứu của bạn là",marks[nums-1][th-1])
        else:
            print("vui lòng nhập đúng cột điểm")
    else:
        print("vui lòng nhập đúng số thứ tự học sinh:")
num=int(input("nhập số thứ tự học sinh cần tra cứu:"))
find(num)
nums=int(input("nhập số thứ tự học sinh cần tra cứu cột điểm:"))
th=int(input("nhập thứ tự cột điểm:"))
finds(nums,th)
# thống kê tên khác nhau của học sinh
realname=[]
for i in range(n):
    if names[i] not in realname:
        realname.append(names[i])
for i in range(len(realname)):
    count=0
    for j in range(n):
        if realname[i]==names[j]:
            count+=1
    print("tên ",realname[i]," lặp lại ", count," lần")
# truy xuất dữ liệu ma trận
s=0
for i in range(n):
    for j in range(len(marks[i])):
                   s+=1
print("tổng số phần tử trong ma trận là", s)
smax=0
for i in range(n):
    if len(marks[i])>smax:
        smax=len(marks)
for i in range(n):
    if len(marks[i])==smax:
        print("dòng có tổng số phần tử lớn nhất là dòng thứ:",i-1,)
real=[]
for i in range(n):
    for j in range(len(marks[i])):
        if marks[i][j] not in real:
            real.append(marks[i][j])
print("các phần tử riêng biệt là",end=" ")
for i in real:
    print(i,end=" ")
print()
def oxy(a):
    dem=0
    toado=[]
    for i in range(n):
        for j in range(len(marks[i])):
            if marks[i][j]==a:
                dem+=1
                x=(i,j)
                toado.append(x)
    print("số ",a,"lặp lại ",dem,"lần tại các điểm",end=" ")
    for i in toado:
        print(i,end=" ")
a=int(input("nhấp số a:"))
oxy(a)