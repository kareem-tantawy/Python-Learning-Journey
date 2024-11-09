# URL: https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/X


# Get input values from the user, separated by spaces
a, b, c, d = map(int, input().split())

# Check if the numbers form a valid increasing sequence
if c >= a and b >= c and d >= b and d >= a:
    # If c is the second largest and b is the smallest, print c and b
    print(f"{c} {b}")
elif c >= a and b >= c and b >= d and d >= a:
    # If c is the second largest and d is the smallest, print c and d
    print(f"{c} {d}")
elif c <= a and b >= c and d >= b and d >= a:
    # If a is the second largest and b is the smallest, print a and b
    print(f"{a} {b}")
elif c <= a and b >= c and d <= b and d >= a:
    # If a is the second largest and d is the smallest, print a and d
    print(f"{a} {d}")
else:
    # If no valid increasing sequence can be formed, print -1
    print(-1)