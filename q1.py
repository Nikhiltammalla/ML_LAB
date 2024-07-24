"1. Write a program to count the number of vowels and consonants present in an input string."
user_input=input("Enter any string:")
l1=[]
abc=list(user_input)
vowels={'a','e','i','o','u'}
vow=0
cons=0
for item in abc:
    item=item.lower()
    if item in vowels:
        vow=vow+1
    else:
        cons=cons+1
print("vowels:",vow)
print("Constants:",cons)
print(abc)