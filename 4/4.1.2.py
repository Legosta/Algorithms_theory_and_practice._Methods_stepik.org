given = input().split()
n, W = int(given[0]), int(given[1])
lst = [[int(i) for i in input().split()] for j in range(n)]
lst.sort(key = lambda cost: cost[0]/cost[1])
max_price = 0
while W and lst:
    if W >= lst[-1][1]:
        max_price += lst[-1][0]
        W -= lst[-1][1]
        del lst[-1]
    else:
        max_price += W * (lst[-1][0]/lst[-1][1])
        break
print('{:.3f}'.format(max_price))