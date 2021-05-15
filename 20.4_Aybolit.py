base = ["Иван", "Юлия Иванкова"]


def hello(name):
    print("Здравствуйте " + name + "! Вашу карту ищут...")


def search_card(name):
    if base.__contains__(name):
        num = base.index(name) + 1
        print("Ваша карта с номером " + str(num) + " найдена")
    else:
        print("Ваша карта не найдена")



hello('Иван&quot')
search_card('Иван')
hello('Юлия Иванова')
search_card('Юлия Иванова')