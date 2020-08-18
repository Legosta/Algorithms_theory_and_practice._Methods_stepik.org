def fib_mod(n, m:int):
    count = 0
    lst = [0, 1]
    for i in range(2, 6*m): # Для всех положительных целых чисел m справедливо неравенство: pi(m) <= 6*m
        lst.append((lst[i-1]+lst[i-2])%m)
        count += 1
        if lst[i] == 1 and lst[i-1] == 0: # Проверка, что остатки от деления на m не начали повторяться
            break
    return (lst[n%count]) # Возвращаем из списка остатков деления искомый остаток, памятуя об их периодичности 


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()