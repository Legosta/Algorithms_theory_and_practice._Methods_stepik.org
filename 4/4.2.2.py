nums = input().split()
d = {}
for _ in range(int(nums[0])):
    char,code = input().split(": ")
    d[char] = code
st = input()

d_v = list(d.values())
start = 0

while not st.isalpha():
    for i in d_v:
        if st.startswith(i, start):
            st = st.replace(i, list(d.keys())[list(d.values()).index(i)],1)
            start += 1
        else:
            pass
print(st)