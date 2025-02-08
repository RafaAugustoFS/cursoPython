for x in range(10):
    for y in range(x+1):
        print("*", end="")
    
    print()
    
print("Digite um numero")
a=int (input())

resto = a % 2

print("Digite um numero")
b=int (input())

if resto == 0:
    for y in range(a, b, +2):
        print(y)
else:
    for y in range(a, b, +2):
        print(y+1)