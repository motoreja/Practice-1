# Практическая работа №1
# Написать программу на Python, которая:
#
# Подсчитывает общее количество символов в файле
# Подсчитывает общее количесто символов без пробелов
# Подсчитывает количество символов без знаков препинания
# Подсчитывает количество слов в файле
# Подсчитывает количество предложений
# Результат подсчета должен быть выведен в консоль


def CollectDict(dict_in, dict_out):
    for i in dict_in:
        if i in dict_out:
            if type(dict_out) == type(dict_in):
                dict_out[i] += dict_in[i]
            else:
                dict_out[i] += 1
        else:
            if type(dict_out) == type(dict_in):
                dict_out |= {i: dict_in[i]}
            else:
                dict_out |= {i: 1}


# открываем файл для чтения
filename = 'aristotle.txt'

print(f'Анализ файла {filename}:\n')

f = open(filename,'r')\

eof = False
sum_of_prep = 0

symb_prep = ['.', '?', '!', ':', ';', ',', '-', '--', '(', ')', '"', '[', ']', '{', '}']

char_dict = dict()
word_dict = dict()
sentance_dict = dict()

while not eof:
    s = f.readline()
    # для подсчета символов воспользуемся map и zip
    s_chars = set(s)
    s_map = list(map(s.count, s_chars))
    s_zip = dict(zip(s_chars, s_map))
    # для подсчета знаков препинания воспользуемся map
    prep_map = list(map(s.count, symb_prep))
    sum_of_prep += sum(prep_map)
    # складываем словари s_zip и char_dict
    CollectDict(s_zip, char_dict)

    # Для подсчета количества слов (что-то разделенное пробелами и знаками препинания) создаем словарь
    # на всякий случай удалим все непечатные символы
    s2 = s
    for i in s_chars:
        if not i.isprintable():
            s2 = s2.replace(i, '')

    s2_list = s2.split(' ')
    CollectDict(s2_list, word_dict)

    # Проверка конца файла
    if s == '':
        eof = True
# определение количества символов
sum_of_symbols = sum_of_symbols2 = 0
for i in char_dict:
    sum_of_symbols += char_dict[i]
    if i != ' ':
        sum_of_symbols2 += char_dict[i]
sum_of_symbols3 = sum_of_symbols - sum_of_prep

# определение количества слов
sum_of_words = 0
sum_of_sentances = 0
for i in word_dict:
    sum_of_words += word_dict[i]
    # подсчет количества предложений (определяется по наличию в конце слова . ! или ? знаков)
    if len(i) > 0:
        if i[-1] == '.' or i[-1] == '!' or i[-1] == '?':
            sum_of_sentances += word_dict[i]

print(f'Общее количество символов: {sum_of_symbols}')
print(f'Количество символов без пробелов: {sum_of_symbols2}')
print(f'Количество символов без знаков препинания: {sum_of_symbols3}')
print(f'Количество слов: {sum_of_words}')
print(f'Количество предложений: {sum_of_sentances}')

# закрываем файл
f.close()

