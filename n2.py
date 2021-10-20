# 5.2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('textfile.txt', 'r') as f:
    text = f.read()
    number_of_lines = 0
    number_of_words = 0
    for r in text:
        if r == ' ':
            number_of_words += 1
        elif r == '\n':
            number_of_lines += 1
            number_of_words += 1
print(text)
print('Слов: ',number_of_words, 'Строк: ', number_of_lines)
