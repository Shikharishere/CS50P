expression = input("Expression: ")

x = float(expression.split()[0])
y = expression.split()[1]
z = float(expression.split()[2])

if '+' in y:
    print(x + z)
elif '*' in y:
    print(x * z)
elif '/' in y:
    print(x / z)
elif '-' in y:
    print(x - z)