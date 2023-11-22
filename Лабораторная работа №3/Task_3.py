import numpy as np
def count_letters(text):
    text2 = text.lower()
    bokl = np.array([])
    bokc = np.array([[]])
    for lett in text2:
        if not lett.isalpha():
            continue
        bokl = np.append(bokl, lett)
    bokl = list(set(bokl))
    bokl = sorted(bokl)

    for i in bokl:
        CL = 0
        for lett in text2:
            if i == lett:
                CL += 1
        bokc = np.append(bokc, CL)

    return bokl, bokc
def calculate_frequency(di, CL):
    for i, j in di.items():
        j = j / CL
        print(i, round(j, 2), sep=": ")

text = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

CL = 0
for i in text:
    if not i.isalpha():
        continue
    CL += 1

letters, count = count_letters(text)

dict_ = dict(zip(letters, count))

calculate_frequency(dict_, CL)