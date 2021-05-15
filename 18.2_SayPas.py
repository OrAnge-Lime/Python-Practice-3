def ask_password():
    pas = 'password'

    for i in range(3):
        inp = input("Password: ")
        if inp == pas:
            print("Пароль принят")
            break
        elif i == 2:
            print("В доступе отказано")

ask_password()