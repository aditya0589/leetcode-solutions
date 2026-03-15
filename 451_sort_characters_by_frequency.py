s = "tree"
count = {}

for element in s:
    count[element] = 0

for element in s:
    count[element] += 1

buckets = {}

for key, value in count.items():
    if value not in buckets:
        buckets[value] = []
    buckets[value].append(key)
    
res = []
for i in range(len(s), 0, -1):
    if i in buckets:
        for c in buckets[i]:
            res.append(c * i)

print("".join(res))
