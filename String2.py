# 2) Вводится строка, состоящая из букв и пробелов. Составить из входящих в нее
#    букв несколько любых их сочетаний (слов) любой длины. Каждую букву строки
#    можно использовать неограниченное количество раз.
import random

sentence = input('Введите строка: ')
sentence_copy = sentence.split()
sentence = ''.join(sentence_copy)
len_sentence = len(sentence)


# сколько слов должны вывести
n = int(input("Сколько слов должны вывести: "))
for i in range(n):
    word = ''   # сочетание несколько любых букв
    len_word = random.randint(3, 6)     # любой длины
    while len_word > 0:
        random_letter = random.randrange(len_sentence)
        word += sentence[random_letter]
        len_word -= 1
    print(f'{i+1} - слово: {word}')



