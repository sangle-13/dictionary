# form initialization
height=int(input("chiều cao của form: "))
width=int(input("chiều rộng của form: "))
# frame initialization
frame=[["13" for i in range(width)] for j in range(height)]
# edit frame
for i in range(height):
    frame[i][4]="  "
    frame[i][10]="  "
    frame[i][18]="  "
    frame[i][23]="  "
    frame[i][29]="  "
for i in range(height-1):
    for j in range(1,4):
        frame[i][j]="  "
for i in range(height):
    if i==0 or i==4:
        frame[i][5],frame[i][9]="  ","  "
    else:
        for j in range(6,9):
            frame[i][j]="  "
for i in range(height):
    for j in range(11,18):
        frame[i][j]="  "
for i in range(height):
    if i==0 or i==1:
        frame[i][11],frame[i][17]="13","13"
    if i==2:
        frame[i][12],frame[i][16]="13","13"
    if i==3:
        frame[i][13],frame[i][15]="13","13"
    if i==4:
        frame[i][14]="13"
for i in range(height):
    if i%2!=0:
        for j in range(20,23):
            frame[i][j]="  "
for i in range(height):
    for j in range(24,29):
        frame[i][j]="  "
for i in range(height):
    for j in range(24,29):
        if j%4==0:
            if i==1 or i==2:
                frame[i][j]="13"
        else:
            if j%2!=0:
                if i==0 or i==3:
                    frame[i][j]="13"
            else:
                if i==1 or i==4:
                    frame[i][j]="13"
for i in range(height-1):
    for j in range(30,34):
        frame[i][j]="  "
for i in range(height):
    frame[i][30],frame[i][33]="13","13"
for i in range(height):
    for j in range(width):
        print(frame[i][j],end=" ")
    print()