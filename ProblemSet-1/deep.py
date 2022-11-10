prompt = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")

if prompt.strip() == '42' or prompt.lower() == 'forty-two' or prompt.lower() == 'forty two':
    print('Yes')
else:
    print('No')