# L = list(map(int, input()))

# if len(L) == 1:
#     print(0) 

# else:
#     count = 0

#     for i in range(1, len(L)):
#         if L[i] == L[0] and L[i-1] != L[i]:
#             count += 1
#     if L[0] != L[-1]:
#         count += 1

#     print(count)

import sys

L = sys.stdin.readline()
count = 0

for i in range(len(L) - 1):
    if L[i] != L[i + 1]:
        count +=1

print(count // 2)