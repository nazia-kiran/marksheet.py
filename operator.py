select = input("operation forms 1,2,3,4 : ")
n = int(input("enter a num : "))
n2 = int(input("enter a num2 : "))
if select == '1':
    print(n, '+' , n2, '=', n+n2)
elif select == '2':
    print(n, '-' , n2,'=', n-n2)
elif select == '3':
    print(n, '*', n2, '=', n*n2)
elif select == '3':
    print(n, '/' , n2, '=', n/n2)
else:
    print("invalid input")
