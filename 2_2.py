depth = 0
dist = 0
aim = 0
while(True):
    readin = input().split(" ")
    if (readin[0] == "forward"):
        dist += int(readin[1])
        depth += aim * int(readin[1])
    elif (readin[0] == "down"):
        aim += int(readin[1])
    elif (readin[0] == "up"):
        aim -= int(readin[1])
    print(depth * dist)