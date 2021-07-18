
path = "C:\\Users\\User\\Desktop\\skillup\\lesson 3-5\\text_1.txt"
path = "C:\\Users\\User\\Desktop\\skillup\\lesson 3-5\\text_2.txt"

file_1 = "text_1.txt"
file_2 = "text_2.txt"

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
    def get_symbols(fl):
        return f'The number of symbols in the file {len(fl.read())}'
    print(get_symbols(file_1))
    file_1.close()

# посчитать количество строк
with open("text_1.txt", mode="r") as file_1:
    def get_strings(fl):
        return f'The number of strings are {len(fl.readlines())}'
    print(get_strings(file_1))
    file_1.close()


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

with open("text_2.txt", mode="r") as file_2:
    def get_longest_line(fl):
        return max(fl.readlines(), key=len)
    print(f'The longest string is: {get_longest_line(file_2)}')
    
    file_2.close()
        

# ==========================================
# =                Task 5                  =
# ==========================================
# Посчитать сколько раз встречается заданное слово

s = open("text_1.txt", mode="r")
file_1 = s.read()
def count_of_words(fl, word = input('Enter tshe word: ')):
    count = 0
    for i in fl:
        if i == word:
            count += 1             
        return count
print(f'The word occurs {count_of_words(fl = file_1)} times in the text')
s.close()



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
