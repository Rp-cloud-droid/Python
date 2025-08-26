# Function to find two odd occurring numbers

def findTwoOdd(arr, size):
   xorof2 = 0
   x = 0
   y = 0
   
   for i in range(size):
    xorof2 = xorof2 ^ arr[i]
    setbit = xorof2 & ~(xorof2 - 1)
    
   for i in range(size):
       
       if arr[i] & setbit:
         x = x ^ arr[i] 
       else:
         y = y ^ arr[i] 
         
         print("The two ODD elements are", x, "and", y)
arr = []
n = int(input("Enter array size: "))
for i in range(n):
   num = int(input("Enter number: "))
   arr.append(num)
   findTwoOdd(arr, n)