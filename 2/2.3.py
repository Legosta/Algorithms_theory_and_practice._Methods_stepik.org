def gcd(a, b):
    while a != 0 and b != 0:
        if a >= b:
            a, b = a%b, b
        else:
            b, a = b%a, a
    return abs(a-b)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()