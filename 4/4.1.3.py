def split_numbers(N):
    lst = []
    i = 1
    while N > i*2:
        N -= i
        lst.append(i)
        i += 1
    else:
        lst.append(N)
    return lst

n = int(input())
print(len(split_numbers(n)))
print(*split_numbers(n))