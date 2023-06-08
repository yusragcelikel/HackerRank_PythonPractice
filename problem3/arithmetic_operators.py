if __name__ == '__main__':

    a = int(input())
    b = int(input())

    # check if the given numbers are in the inclusive range of 1 to 10 billion
    if a < 1:
        print("You've entered invalid value.")
    elif a > 10 ** 10:
        print("You've entered invalid value.")
    elif b < 1:
        print("You've entered invalid value.")
    elif b > 10 ** 10:
        print("You've entered invalid value.")

    # the task we've asked for:
    else:
        add = a + b
        sub = a - b
        mult = a * b

        print(add)
        print(sub)
        print(mult)
