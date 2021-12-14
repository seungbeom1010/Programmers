
n = list(map(int, input()))

R = n[:(len(n)//2)] #자릿수 기준 왼쪽 숫자리스트
L = n[(len(n)//2):] #자릿수 기준 오른쪽 숫자리스트

if sum(R) == sum(L):
    print('LUCKY')
else:
    print('READY')
