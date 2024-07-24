'''4. Write a program that accepts a matrix as input and returns its transpose'''
matrix1=[]
trans=[]
row_A = int(input("Enter the No. of rows for matrix1:"))
col_A = int(input("Enter the no. of columns for matrix1:"))
for i in range(row_A):
    rows=[]
    for j in range(col_A):
        print(f"Enter value for {i+1}{j+1}")
        a=int(input())
        rows.append(a)
    matrix1.append(rows)
trans=[]
for a in range(col_A):
    row=[]
    for b in range(row_A):
        row.append(0)
    trans.append(row)

for i in range(row_A):
    for j in range(col_A):
        trans[j][i]=matrix1[i][j]
for m in trans:
    print(m)
