with open('blist.in', 'r') as f:
    lines = f.readlines()

number_of_cows = int(lines[0])
cows = []

for i in range(1, number_of_cows + 1):
    start, end, buckets = lines[i].strip().split()
    start = int(start)
    end = int(end)
    buckets = int(buckets)
    cows.append([start, end, buckets])
print(cows)

maximum_time = 0
for i in range(len(cows) - 1):
    if cows[i + 1][1] > cows[i][1]:
        maximum_time = cows[i + 1][1]
print(maximum_time)

buckets = []
for i in range(maximum_time):
    buckets_needed = 0
    for j in range(len(cows)):
        if cows[j][0] <= i <= cows[j][1]:
            buckets_needed += cows[j][2]
    buckets.append(buckets_needed)
print(buckets)

maximum_buckets = 0
for i in range(len(buckets)):
    if buckets[i] > maximum_buckets:
        maximum_buckets = buckets[i]
print(maximum_buckets)

with open('blist.out', 'w') as f:
    f.write(str(maximum_buckets))