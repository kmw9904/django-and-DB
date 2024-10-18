import sys
N = int(sys.stdin.readline().strip())
array = []
for _ in range(N):
    array.append(int(sys.stdin.readline().strip()))

result = [0] * ( max(array) + 1)

for i in range(len(array)):
    result[array[i]] += 1

for i in range(len(result)):
    for j in range(result[i]):
        print(i)