#Another way to check if the no is even or odd

num = int(input("Enter a number:"))
if(num == 0):
    print("Zero is not even and odd no")
else:
    temp = num%10
    if(temp == 0 or temp == 2 or temp == 4 or temp == 6 or temp == 8):
        print("Even number")
    else:
        print("Odd number")
"""
In this program it is checking whether the last element of given no is 0,2,4,6,8 if it is then its even number otherwise it is odd according to divisibility rule of two
"""
