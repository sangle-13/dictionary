#input
N=int(input("nhập số tự nhiên N:"))
if N <=0 or N > 100:
    print("vui lòng nhập số tự nhiên N trong khoảng 0 < N <=100 ")
else:
    strings=input("nhập dãy số gồm "+ str(N)+" số nguyên:")
    List_input=[int(x) for x in strings.split()]
#main_program
    Max_index=List_input[0]
    for x in List_input:
        if x > Max_index:
            Max_index=x
    List_output=[]
    for i in range(N):
        index_test=[]
        for j in range(List_input[i]):
            index_test.append("*")
        if len(index_test)< Max_index:
            for i in range(len(index_test),Max_index):
                index_test.insert(0," ")
        List_output.append(index_test)
    List_output_real=[]
    for i in range(Max_index):
        List_fake=[]
        for j in range(N):
            List_fake.append(List_output[j][i])
        List_output_real.append(List_fake)
#output
    for i in range(Max_index):
        for j in range(len(List_output_real[i])):
           print(List_output_real[i][j],end="")
        print()
