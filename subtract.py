# Subtracting of 2 numbers

a =int(input('Enter Value for A: '))
b= int(input('Enter Value for B: '))
d = input('Enter Arthematic operator to perform:')
if d=='*' :
    c= a*b
elif d=='+':
    c= a+b
elif d=='-':
    c=a-b
elif d=='/':
    c=a/b

print(c)