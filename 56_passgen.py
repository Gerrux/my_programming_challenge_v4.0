from random import randrange
alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9'
symbols='! " # $ % & ( ) * + , - . / : ; < = > ? @ [ ] ^ _ ` { | } ~'
alphabet = alphabet.split(" ")
symbols = symbols.split()
data = []

question = input('Вы хотите сделать сложный пароль или нет? (да/нет)\n')
lenghtpass = int(input('Длина вашего пароля:\n'))
if question.lower() == "да":
    data = alphabet + symbols
else:
    data = alphabet
def passgen(data, lenghtpass):
    password = ''
    for i in range(1, lenghtpass+1):
        number = randrange(1, len(data))
        password+=data[number]
    return password
    

password = passgen(data, lenghtpass)
print(password)