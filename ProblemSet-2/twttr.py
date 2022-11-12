# prompting user for input
Input = input("Input: ")

# vowel list
vowels = ['a', 'e', 'i', 'o', 'u']

for i in Input:
    if i.lower() in vowels:
        Input = Input.replace(i, "")
print(f"Output: {Input}")