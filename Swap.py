def swap1(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("Before Swapping : a = ", a, " b =", b)

def swap2(a,b):
    a = (a & b) + (a | b)
    b = a + (~b) + 1
    a = a + (~b) + 1
    print("After Swapping: a = ", a, " b =", b)

swap1(1,2)
swap2(2,1)