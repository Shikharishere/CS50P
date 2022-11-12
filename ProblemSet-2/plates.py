# main function
illegal_symbols = [' ', '.', ',', "'"]

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("valid")
    else:
        print("Invalid")

def is_valid(s):

    total_numbers_checked = 0
    validated_string = ""
    if 6 >= len(s) >= 2:
        if s[0].isalpha() and s[1].isalpha():
            for i in s:
                if i not in illegal_symbols:
                    # if letter is numeric and is not zero
                    if i.isnumeric() and total_numbers_checked == 0 and i != '0':
                        # total numbers checked so far in the string
                        total_numbers_checked += 1
                        # adding this letter to the validated string
                        validated_string += i
                    # if letter is numeric and can be zero
                    elif i.isnumeric() and total_numbers_checked > 0:
                        total_numbers_checked += 1
                        validated_string += i
                    # if letter is alphabatic and no numbers were found till now
                    elif i.isalpha() and total_numbers_checked == 0:
                        validated_string += i
    # if string validated is equal to the string provided by the user
    if validated_string == s:
        return True
    else:
        return False

main()