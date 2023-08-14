x = input("işlemek istediğiniz sayıyı girin :")
y = input("işlemek istediğiniz ikinci sayıyı girin:")
c = input("yapılacak işlemi seçin:")
x = int(x)
y = int(y)
result = ""
if (c == "/"):
    result = x / y
elif(c == "*"):
    result = x * y
elif(c == "+"):
    result = x + y
elif(c == "-"):
    result = x - y
else:
    print("geçerli bir sayı girmediniz")

print(result)