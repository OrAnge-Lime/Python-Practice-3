def month_name(num, l):
    ru = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь",
          "нояюрь", "декабрь"]
    en = ["january", "february", "march", "may", "june", "july", "august", "september", "october",
          "november", "december"]

    if l == "ru":
        return ru[int(num)+1]
    else:
        return en[int(num)+1]