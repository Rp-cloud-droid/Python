limit=int(input("enter the limit: "))
print("sum of integer numbers")
sum =0
for i in range(1, limit+1):
    sum = sum+i
print("sum of ", limit, " = ", sum)