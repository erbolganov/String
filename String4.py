# 4) Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
#    Например, если было введено "abc cde def", то должно быть выведено "abcdef".

sentence = input("Введите строка: ")
sentence = sentence.replace(" ", "")
print(sentence)
w = []
for item in sentence:
    if not(item in w):
        w.append(item)
print('Резултат:', ''.join(w))