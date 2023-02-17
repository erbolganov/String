# 7) Вводится строка слов, разделенных пробелами. Найти самое длинное слово
#    и вывести его на экран. Случай, когда самых длинных слов может быть несколько,
#    не обрабатывать.
sentence = input('Enter the sentence: ')
sentence = sentence.split()
max_len = sentence[0]
for i in range(1, len(sentence)):
   if len(max_len) < len(sentence[i]):
      max_len = sentence[i]

print('Max word:', max_len)