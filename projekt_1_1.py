words_len = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0, "13": 0}
if word not in words_len and len(word) == 1:
        words_len["1"] += 1
    elif word not in words_len and len(word) == 2:
        words_len["2"] += 1
    elif word not in words_len and len(word) == 3:
        words_len["3"] += 1
    elif word not in words_len and len(word) == 4:
        words_len["4"] += 1
    elif word not in words_len and len(word) == 5:
        words_len["5"] += 1
    elif word not in words_len and len(word) == 6:
        words_len["6"] += 1
    elif word not in words_len and len(word) == 7:
        words_len["7"] += 1
    elif word not in words_len and len(word) == 8:
        words_len["8"] += 1
    elif word not in words_len and len(word) == 9:
        words_len["9"] += 1
    elif word not in words_len and len(word) == 10:
        words_len["10"] += 1
    else: 
        words_len["11"] += 1


print(words_len) 


lenght = list(words_len.values())

result = {}

for len in lenght:
    if len not in result:
        result[len] = 1
    else:
        result[len] += 1


result_sort = sorted(result.items())
print(result_sort)

for index, tupl in enumerate(result_sort, 1):
    print(oddelovac)
    print(f"|{index}.|{tupl[1]}|")
    print(oddelovac)
slovnik = {"the": 3, "the": 3}
print(slovnik)

words_len = {}
for word in words_only:
    words_len[word] = len(word) #!!! nevloží se opakující se slova, vyzkoušena vorba listu  i tuplu
print(words_len)