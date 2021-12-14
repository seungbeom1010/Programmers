from itertools import *

n, m = map(int, input().split())

L = [] #지도 리스트로 받기

for _ in range(n):
    L.append(list(map(int, input().split())))

houses = [] # 집 좌표 모음
chickens = [] # 치킨집 좌표 모음

for i in range(len(L)):
    for j in range(len(L)):
        if L[i][j] == 1:
            houses.append([i + 1, j + 1])
        elif L[i][j] == 2:
            chickens.append([i + 1, j + 1])
        else:
            continue


selected_chickens = list(combinations(chickens, m)) #살아남은 m 개의 치킨집 조합

result = []

for c_comb in selected_chickens:
    temp1 = [] #해당 치킨집 조합 별 집과 치킨집 최소거리 모음
    for house in houses: 
        temp2 = []
        for c in c_comb:
            A = abs(house[0] - c[0]) + abs(house[1] - c[1])
            temp2.append(A)
        temp1.append(min(temp2))
    result.append(sum(temp1))

print(min(result))
        
        
