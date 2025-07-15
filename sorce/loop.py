a = int(input("작은 수 a : "))
b = int(input("큰 수 b : "))
sum = 0

while( a <= b):
    print("sum = ", sum, " + ", a, " -> ", sum + a)
    sum = sum + a
    a = a + 1

print(sum)
 
