values = len("011001011100")
gamma_rate = [0] * values
epsilon_rate = [0] * values
lines = 0

arr = []
track = [0] * values

while True:
    arr = list(input())
    if (len(arr) == 0):
        break
    for x in range(len(arr)):
        if (arr[x] == '1'):
            track[x] += 1
    lines += 1

for x in range(len(track)):
    if (2 * track[x] > lines):
        gamma_rate[x] = '1'
        epsilon_rate[x] = '0'
    else:
        gamma_rate[x] = '0'
        epsilon_rate[x] = '1'

print(int("".join(str(x) for x in epsilon_rate),2) * int("".join(str(x) for x in gamma_rate),2))