window = [-1] * 3
count = 0
sum = 0
prevSum = float("inf")
while(True):
    window[0] = window[1]
    window[1] = window[2]
    window[2] = int(input())
    if (window[0] != -1):
        sum = window[0] + window[1] + window[2]
        if (sum > prevSum):
            count += 1
        prevSum = sum
        print(count)