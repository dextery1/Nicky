x = int(input("Enter a number:\n"))
rev = 0
while x > 0:
    rev = rev * 10 + x % 10
    print(rev)
    x = x // 10
    print(x)
print("Reversed number", rev)