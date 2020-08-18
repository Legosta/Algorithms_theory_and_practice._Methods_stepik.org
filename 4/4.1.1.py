n = int(input())
dots = []
cuts = [[int(i) for i in input().split()] for j in range(n)] 
cuts.sort(key = lambda elem: elem[1])

i, j = 0, 0
while j < len(cuts):
    if cuts[j][0] <= cuts[i][1] <= cuts[j][1]:
        j+=1
    else:
        dots.append(cuts[i][1])
        i = j
else:
    dots.append(cuts[i][1])
print(str(len(dots))+'\n'+" ".join(str(i) for i in dots))