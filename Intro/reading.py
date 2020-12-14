f = open('scores.txt', 'r')

participants = {}

for line in f:
    entry = line.strip().split(',')
    participant = entry[0]
    score = entry[1]
    participants[participant] = score
    print(participant + ": " + score)
f.close()

print(participants)