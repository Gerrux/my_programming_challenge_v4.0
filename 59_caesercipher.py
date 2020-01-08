dataUp = ['X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C']
dataDown = ['x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c']
text = list(input('Введите слово:\n'))
answer = ''
# Crypting
for i in range(len(text)):
    if text[i] in dataUp:
        idletter = dataUp.index(text[i])
        answer += dataUp[idletter+3]
    elif text[i] in dataDown:
        idletter = dataDown.index(text[i])
        answer += dataDown[idletter+3]
    else:
        answer += text[i]
print(answer)

#Encrypting
answer = ''
dataUp.reverse()
dataDown.reverse()
for i in range(len(text)):
    if text[i] in dataUp:
        idletter = dataUp.index(text[i])
        answer += dataUp[idletter+3]
    elif text[i] in dataDown:
        idletter = dataDown.index(text[i])
        answer += dataDown[idletter+3]
    else:
        answer += text[i]

print(answer)