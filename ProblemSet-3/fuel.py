def main():
        gauge_output = get_fuel_gauge()
        if 99 <= gauge_output <= 101:
            print("F")
        elif gauge_output <= 1:
            print("E")
        else:
            print(str((gauge_output)) + "%")



def get_fuel_gauge():
    while True:
        # trying
        try:
            a = input("Fraction: ")
            X = int(a[0:a.index('/')])
            Y = int(a[(a.index('/') + 1):])
            num = round((X/Y)*100)
        # if error
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        # if no exceptions
        else:
            break
    return num

main()