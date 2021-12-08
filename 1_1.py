
import math

prev = float("inf")
curr = 0
count = 0
while(True) :
    curr = int(input())
    if (curr > prev) :
        count += 1
    prev = curr
    print(count)