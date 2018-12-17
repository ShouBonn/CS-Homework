from random import randint
with open('backforth.in', 'r') as f:
    lines = f.readlines()
barn1 = lines[0].strip().split()
barn2 = lines[1].strip().split()
print(barn1, barn2)

tank1 = 1000

differ_buckets1 = []
for item in barn1:
    if item not in differ_buckets1:
        differ_buckets1.append(item)

differ_buckets2 = []
for item in barn2:
    if item not in differ_buckets2:
        differ_buckets2.append(item)

print(differ_buckets1, differ_buckets2)

# length = len(barn1)
#
# for i in range(length):
#     a = randint(0, 9)
#     tank1 -= int(barn1[a])
#     barn2.append(barn1[a])
#     barn1.pop(a)
#
#     print(barn1, barn2, tank1)
#
#     b = randint(0, 9)
#     tank1 += int(barn2[b])
#     barn1.append(barn2[b])
#     barn2.pop(b)
#
#     print(barn1, barn2, tank1)
#
#     c = randint(0, 9)
#     tank1 -= int(barn1[c])
#     barn2.append(barn1[c])
#     barn1.pop(c)
#
#     print(barn1, barn2, tank1)
#
#     d = randint(0, 9)
#     tank1 += int(barn2[c])
#     barn1.append(barn2[c])
#     barn2.pop(c)
#
#     print(barn1, barn2, tank1)
#

x = (len(differ_buckets1) + 1) * (len(differ_buckets2) + 1) - 1

with open('backforth.out', 'w') as f:
    f.write(str(x))