def powerOf4(number):
    if(number <= 0):
        return False
    if (number & (number - 1)):
        count = 0
        while(number > 1):
            number >>= 1
            count += 1

        return count % 2
        
number = int(input("Enter your number : "))
if(powerOf4(number)):
     print(number, 'is a power of 4')
else:
     print(number, 'is not a power of 4')