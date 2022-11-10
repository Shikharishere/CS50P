def main():
    t = input("What time is it? ")
    timing = convert(t)

    if 7.00 <= timing <= 8.00:
        print('breakfast time')
    elif 12.00 <= timing <= 13.00:
        print('lunch time')
    elif 18.00 <= timing <= 19.00:
        print('dinner time')


def convert(time):
    ind = time.index(':')
    hours = int(time[:ind])
    minutes = int(time[ind + 1:])
    return (hours + (minutes/60))

if __name__ == "__main__":
    main()