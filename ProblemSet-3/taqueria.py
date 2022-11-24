def felipes_taqueria():
    # item:price mapping
    food_items  = {
            "Baja Taco": 4.00,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
            }
    # defining the order_total variable
    order_total = 0
    while True:
        try:
            # propting user for input
            user_input = (input("Item: ")).title()
            # if item in food_item dict
            if user_input in food_items:
                # then add the price of the item to the order_total variable
                order_total += food_items[user_input]
                # print the order_total after each item order
                print(f"Total: ${order_total}0")
        # if ctrl + D is pressed then 
        except EOFError:
            print()
            break
felipes_taqueria()