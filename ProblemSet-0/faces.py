# convert function
def convert(s):
    s = s.replace(":)", "🙂")
    s = s.replace(":(", "🙁")
    return s

# main function
def main():
    # prompting the user
    prompt = input()

    # calling convert function and printing the output
    print(convert(prompt))

# calling the main function
main()