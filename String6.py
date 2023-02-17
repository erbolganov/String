# 6) Вводится строка, содержащая буквы, целые неотрицательные числа и иные символы.
#    Требуется все числа, которые встречаются в строке, поместить в отдельный
#    целочисленный массив. Например, если дана строка "data 48 call 9 read13 blank0a",
#    то в массиве должны оказаться числа 48, 9, 13 и 0.

sentence = input("Enter the sentence: ")
sentence = sentence.split()
print(sentence,'\n--------------------------------------')
num = []

for item in sentence:
    q = ''
    for i in range(len(item)):
        if '0' <= item[i] <= '9':
            q += item[i]
        elif q != '':
            num.append(q)
            q = ''
    if q == '':
        continue
    num.append(q)
print(num)