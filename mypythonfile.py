def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

x = int(input("enter a number"))
y = int(input("enter another number"))

print(f"{x} + {y} = {add(x,y)}")
print(f"{x} - {y} = {sub(x,y)}")
print(f"{x} * {y} = {mul(x,y)}")
print(f"{x} / {y} = {div(x,y)}")