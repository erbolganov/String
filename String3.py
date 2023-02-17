# 3) Вводится строка. Удалить из нее все пробелы. После этого определить,
#    является ли она палиндромом (перевертышем), т.е. одинаково пишется как
#    с начала, так и с конца.

sentence = input('Введите строка: ')
sentence = sentence.replace(" ", "")
len_sentence = len(sentence)

for i in range(len_sentence // 2):
    if sentence[i] != sentence[-1-i]:
        print('Нет, это слово не является палиндромом! ')
        break
    elif i == (len_sentence // 2) - 1:
        print('Да, это слово является палиндромом')