binary=input("Enter binary number: ")
def binarytodecimal(binary):
    decimal =0
    binary = binary[::-1]
    for i in range(len(binary)):
        if binary[i]=="1":
            decimal = decimal + 2 ** 1
        return decimal
        print(f"conversion of {binary} to decimal", binarytodecimal(binary))