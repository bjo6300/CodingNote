import sys
input = sys.stdin.readline

n = int(input().rstrip())
n_card = input().rstrip().split()
m = int(input().rstrip())
m_card = input().rstrip().split()

sangun_card = {}

for card in n_card:
    if card in sangun_card:
        sangun_card[card] += 1
    else:
        sangun_card[card] = 1

answer = []

for num_card in m_card:
    answer.append(sangun_card.get(num_card, 0))

print(*answer)