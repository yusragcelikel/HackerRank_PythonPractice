if __name__ == '__main__':
    n = int(input())

    if n >= 1:
        if n <= 150:
            i = 1
            while i <= n:
                string_i = str(i)
                print(string_i, end="")
                i += 1