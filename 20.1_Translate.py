def translate(text):
    res = ""
    a = "уУеЕаАоОэЭяЯиИюЮ"
    for i in range(text.__len__()):
        if not a.__contains__(text[i]):
            if text[i] != " " or not res.endswith(" "):
                res += text[i]

    return res


translatedText = translate('Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно '
                           'просто читать. Достаточно небольшой тренировки - и вы сможете это делать.')
print(translatedText)
