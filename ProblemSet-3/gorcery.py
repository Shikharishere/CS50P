def grocery():
    # defining new dict here
    item_dict = dict()
    while True:
        try:
            #  prompting the user 
            item = input("")
            if item in item_dict.keys():
                item_dict[item] += 1
            else:
                item_dict[item] = 1
        # if ctrl + D is pressed from the user then 
        except EOFError:
            for key, value in sorted(item_dict.items()):
                print(value, key.upper())
            break
# calling the function
grocery()