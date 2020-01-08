# Готов к графической оболочке

text = input("Введите текст который хотите закодировать:\n")
text = list(text)

# Binary coding (unicode)
def binaryCode(text):
    bufer = []
    for i in range(len(text)):  
        number = str(bin(ord(text[i]))[2:])
        bufer.append(number.upper())
    answer = " ".join(bufer)
    return answer

# Hexadecimal coding
def hexademicalCode(text):
    bufer = []
    for i in range(len(text)):
        number = "0"+str(hex(ord(text[i]))[2:])
        bufer.append(number[1:].upper())
    answer = " ".join(bufer)
    return answer

print(binaryCode(text))
print(hexademicalCode(text))