def outdated():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    # month-day-year format
    while True:
        try:
            # prompting for date and using strip method so that unecessary spaces in the input doesn't produce bugs in the program
            date = input("Date: ").strip()
            if '/' in date:
                year = int(date[-4:])
                month = int(date[0:date.index('/')])
                day = int(date[date.index('/') + 1: -5])

            else:
                year = int(date[-4:])
                month = months.index(date[0:date.index(" ")]) + 1
                day = int(date[(date.index(" ")) + 1:date.index(",")])
        # if ValueError then
        except ValueError:
            pass

        else:
            if month <= 12 and day <=31:
                # here 02 is used so that if month and day are less than 10 then 0 comes before them
                # else it won't
                print(f"{year}-{month:02}-{day:02}")
                break
# calling the functon
outdated()