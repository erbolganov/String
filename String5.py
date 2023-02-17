# 5) Найти в строке указанную подстроку и заменить ее на новую. Строку,
#    ее подстроку для замены и новую подстроку вводит пользователь.

sentence = input("Enter the sentence: ")
change_word = input('Enter the changing word: ')
new_word = input('Enter the new word: ')
sentence = sentence.replace(change_word, new_word)
print('Sentence is changed:', sentence)