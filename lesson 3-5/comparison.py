
path = "C:\\Users\\User\\Desktop\\skillup\\lesson 3-5\\text_1.txt"
path = "C:\\Users\\User\\Desktop\\skillup\\lesson 3-5\\text_2.txt"

# file_1 = "text_1.txt"
# file_2 = "text_2.txt"

# ============================================
# =                 Task 2                   =
# ============================================

# прочитать содержимое файлов
with open("text_1.txt", mode="r") as file_1:
    print(file_1.read())
    file_1.close()

with open("text_2.txt", mode="r") as file_2:
    print(file_2.read())
    file_2.close()

# посчитать количесво символов
with open("text_1.txt", mode="r") as file_1:
    print(f'The number of symbols in the file {len(file_1.read())}')
    file_1.close()

# посчитать количество строк
with open("text_1.txt", mode="r") as file_1:
    print(f'The number of strings are {len(file_1.readlines())}')


# посчитать количество гласных, согласных букв и цифр
s = open("text_1.txt", mode="r")
file_1 = s.read()
def counter(text, lis):
    count = 0
    for i in text:
        if i in lis:
            count += 1
    return count
vowels = "aiuoe"
numbers = "123456789"
consonants = "bcdfghjklmnpqrstvwxyz"
a = counter(file_1, vowels)
b = counter(file_1, numbers)
c = counter(file_1, consonants)
print(f'Number of vowels in the text = {a}')
print(f'Number of numbers in the text = {b}')
print(f'Number of consonants in the text = {c}')
s.close()

# ===================================
# =          Task 1                 =
# ===================================
# Выяснить, совпадают ли их строки.
# Если нет, то вывести несовпадающее строки из каждого файла.

s_1 = open("text_1.txt", mode="r")
s_2 = open("text_2.txt", mode="r")

lines_1 = s_1.readlines()
lines_2 = s_2.readlines()
dif = []

def compare(list_1, list_2):
    for l in lines_1:
        if l not in lines_2:
            dif.append(l)
    return dif
compare(lines_1, lines_2)
print(f'Mismatched strings: {dif}')
s_1.close()
s_2.close()

# ========================================
# =              Task 3                  =
# ========================================

# Удалить файла последнюю строку файла, результат записать в другой файл

s_1 = open("text_1.txt", mode="r")
a = s_1.read()

s_2 = open("text_2.txt", mode="w")
for x in a[:-1]:
    s_2.write(f'{x}')
s_2 = open("text_2.txt", mode="r")

s_1.close()
s_2.close()

# ==========================================
# =              Task 4                    =
# ==========================================
# найти самую длинную строку

s_2 = open("text_2.txt", mode="r")
content = s_2.readlines()
longest_line = max(content, key=len)
print(f'The longest string is: {longest_line}.It has {len(longest_line)}')

s_2.close()
        

# ==========================================
# =                Task 5                  =
# ==========================================
# Посчитать сколько раз встречается заданное слово


s_1 = open("text_1.txt", mode="r")
content = s_1.read()
count = 0
word = input('Enter the word: ')
for i in content:
    if i == word:
        count += 1
print(f'The word {word} occurs {count} times in the text')


# =============================================
# =                  Task 6                   =
# =============================================
# найти и заменить заданное слово

with open("text_1.txt", mode="r") as file_1:
    content = file_1.read()
    content = content.replace('melon', 'apricot')
with open("text_1.txt", mode="w") as file_1:
    file_1.write(content)
with open("text_1.txt", mode="r") as file_1:
    print(file_1.read())
