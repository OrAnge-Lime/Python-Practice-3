person = []

while True:
    comand = input()

    if comand.startswith("setup_profile"):
        person.clear()
        person.append(comand.split('"')[1])
        person.append(comand.split('"')[3])
    elif comand.startswith("print_application_for_leave"):
        print("Заявление на отпуск в период " + person[1] + ". " + person[0])
    elif comand.startswith("print_holiday_money_claim"):
        print("Прошу выплатить " + comand.split('"')[1] + " отпускных денег. " + person[0])
    else:
        print("На время отпуска в период " + person[1] + " моим заместителем назначается " +
              comand.split('"')[1] + ". " + person[0])

