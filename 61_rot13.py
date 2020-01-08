up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
down = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
word = input("Введите слово:\n").upper()
answer = ""
for i in range(len(word)):
    if word[i] in up:
        idletter = up.index(word[i])
        answer += down[idletter]
    elif word[i] in down:
        idletter = down.index(word[i])
        answer += up[idletter]
    else:
        answer += word[i]
print(answer)