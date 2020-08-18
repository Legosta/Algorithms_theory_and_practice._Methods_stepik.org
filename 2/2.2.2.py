def fib_digit(n):
    if n < 2:
        return n
    lst = [None] * n
    lst[0] = 1
    lst[1] = 1
    for i in range(2, n):
        lst[i] = (lst[i-1] + lst[i-2])%10
    return lst[n-1]


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()