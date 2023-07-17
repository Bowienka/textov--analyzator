"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Helena Vyplelová
email: vyplelhel@seznam.cz
discord: Helena V.#7354
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# 1. input přihlašovací jméno a heslo
#+------+-------------+
#| user |   password  |
#+------+-------------+
#| bob  |     123     |
#| ann  |   pass123   |
#| mike | password123 |
#| liz  |   pass123   |
#+------+-------------+
user = {"bob": "123", "ann" : "pass123", "mike": "password123", "liz": "pass123"}

name = input("Zadej jméno: ")

if name in user.keys():
    password = input("Zadej heslo: ")
else:
    print("unregistered user, terminating the program..")
    quit()

if (name, password) in user.items(): #https://note.nkmk.me/en/python-dict-in-values-items/
    print(f"Welcome to the app, {name}.")
    print("We have 3 texts to be analyzed.")
else:
    print("unregistered user, terminating the program..")
    quit()

oddelovac = "-"*40

print(oddelovac)
# pokud jméno a heslo nesouhlasí, upozorní: unregistered user, terminating the program.. a ukonči program (quit), jinak pokračuj.
# 2. uživatel si vybere mezi třemi text (input: Vyber si text: 1, 2, 3) - je třeba posunout indexování, pokud zadá špatné číslo nebo jiný vstup (if vstup not range(1,3), program uživatele upozorní a ukončí se

text = int(input("Enter a number btw. 1 and 3 to select: "))
if int(text) >= 1 and int(text) <= 3:
    text_ed = TEXTS[int(text) - 1]
print(oddelovac)

# 3. pro vybraný text program spočítá:
#   a) počet slov
#   b) počet slov začínajících velkým písmenem,
#   c) počet slov psaných velkými písmeny,
#   d) počet slov psaných malými písmeny,
#   e) počet čísel (ne cifer),
#   f) sumu všech čísel (ne cifer) v textu.

words = text_ed.split() # deafultně odděluje pomocí mezer, složitěji (" ")
words_ed = []
words_only = []
titles = []
uppers = []
lowers = []
numbers = []
figures = []

for word in words:
    words_ed.append(word.strip(".,:;"))
print(f"There are {len(words_ed)} words in selected text.")

for word in words_ed:
    if word.isalpha():
        words_only.append(word)

for word in words_only:
    if word.islower():
        lowers.append(word)
    elif word.isupper():
        uppers.append(word)
    else: 
        titles.append(word)

print(f"There are {len(titles)} titlecase words.")
print(f"There are {len(uppers)} uppercase words.")
print(f"There are {len(lowers)} lowecase words.")

for word in words_ed:
    if word.isnumeric():
        numbers.append(word)

print(f"There are {len(numbers)} numeric strings.")

for number in numbers:
    figures.append(int(number))
print(f"The sum of all numbers {sum(figures)}.")
print(oddelovac)

# g) délka jednotlivých slov ve sloupcovém grafu

#words_len = enumerate(words_only)
#for index, word in words_len:
#   index = len(word)
 #   print(words_len)

words_len = []
for word in words_only:
    word = len(word)
    words_len.append(word)  #!!! nevloží se opakující se slova, vyzkoušena vorba listu  i tuplu


result = {}
for len in words_len:
    if len not in result:
        result[len] = 1
    else:
        result[len] += 1

occurences = "LEN|   OCCURENCES   |NR."
print(occurences)

result_sort = sorted(result.items())
for index, tupl in result_sort:
    star = "*"*int(tupl)
    print(f"{index:3}|{star:16}|{tupl:3}")


