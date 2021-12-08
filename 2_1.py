depth = 0
dist = 0
while(True):
    readin = input().split(" ")
    if (readin[0] == "forward"):
        dist += int(readin[1])
    elif (readin[0] == "down"):
        depth += int(readin[1])
    elif (readin[0] == "up"):
        depth -= int(readin[1])
    print(depth * dist)