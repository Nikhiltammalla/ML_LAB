'''3. Write a program to find the number of common elements between two lists. The lists
contain integers.'''
l1=[1,2,3]
l2=[2,3,4]
com=[]
for i in l1:
    for j in l2:
        if i==j:
            com.append(i)
for b in com:
    print(b)