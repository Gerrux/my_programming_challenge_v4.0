data = []
number = float(input("Введите число до 100000:\n")) 
source = int(number)
if int(number) < 100000:
    for i in range(2, int(number+1)):
        # пробегаем по списку (lst) простых чисел
        for j in data:
            if i % j == 0:
                break
        else:
            data.append(i)
    multiplier = []
    while number != 1:
        for i in range(len(data)):
            if float(number/data[i])-round(float(number/data[i])) == 0:
                multiplier.append(data[i])
                number = number/data[i]
    stroka = str(multiplier[0])
    for a in range(1, len(multiplier)):
        stroka += ' * ' +str(multiplier[a])
    print(str(source) + ' = ' + stroka)
else:
    print("Слишком большое число, вам не хватит вычислительных мощностей!")
