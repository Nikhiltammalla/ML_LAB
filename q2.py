import numpy as np
matrix1=[]
matrix2=[]
row_A = int(input("Enter the No. of rows for matrix1:"))
col_A = int(input("Enter the no. of columns for matrix2:"))
for i in range(row_A):
    rows=[]
    for j in range(col_A):
        print(f"Enter value for {i+1}{j+1}")
        a=int(input())
        rows.append(a)
    matrix1.append(rows)
row_B = int(input("Enter the No. of rows for matrix1:"))
col_B = int(input("Enter the no. of columns for matrix2:"))
for i in range(row_B):
    rows=[]
    for j in range(col_B):
        print(f"Enter value for {i+1}{j+1}")
        b=int(input())
        rows.append(b)
    matrix2.append(rows)
print(matrix1)
print(matrix2)


if col_A != row_B:
    print("Matrix multiplication is not possible")
else:
    maultipication=np.dot(matrix1,matrix2)

print(maultipication)