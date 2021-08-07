N,M = map(int, input().split())

card = list(map(int, input().split()))

result = 0

for i in range(0, len(card)-2):
    for j in range(i+1, len(card)-1):
        for k in range(j+1, len(card)):
            sumCard = card[i] + card[j] + card[k]
            if(sumCard <= M):
                result = max(result, sumCard)

print(result)