# URL: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/Y

a, b, c, d = map(int, input().split())
num = a*b*c*d
num %= 100
print(f"{num:02d}")