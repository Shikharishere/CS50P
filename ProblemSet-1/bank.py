greeting = input("Greeting: ")

if 'hello' in greeting.lower():
    price = 0
elif greeting.lower()[0] == 'h':
    price = 20
else:
    price = 100
print(f"${price}")