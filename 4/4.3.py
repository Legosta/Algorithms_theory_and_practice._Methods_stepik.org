import heapq
import sys

def Insert(x):
    global lst
    heapq.heappush(lst, x*(-1)) 

def ExtractMax():
    global lst
    return heapq.heappop(lst)*(-1)

lst = []
heapq.heapify(lst)

num = int(input())

for _ in range(num):
    line = input().split()
    if line[0] == "Insert":
        op = Insert
        op(int(line[1]))
    else:
        print(ExtractMax())