
n = int(input("Enter how many elements : "))
l = []
for i in range(n):
    l.append(int(input()))
for i in range(n - 1):
    for j in range(n - i - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]

for i in range(n):
    print(l[i], ", ", end="")
