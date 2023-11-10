num = int(input("Enter the integer you want to reverse : "))
n1 = 0
while num > 0:
    rem = num % 10
    num = num // 10
    n1 = n1 * 10 + rem
print(n1)



