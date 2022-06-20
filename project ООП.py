from datetime import timedelta
import datetime
import random
import json

clients = []
admin = []
date = datetime.date.today()
date2 = (date + timedelta(days=random.randint(1, 5))).strftime("%d.%m.%Y")
date = date.strftime("%d.%m.%Y")


class Receipt:
    count = 1

    def __init__(self, receipt_number, product_type, date_of_receipt, date_of_completion, full_name, status):
        self.receipt_number = receipt_number
        self.product_type = product_type
        self.date_of_receipt = date_of_receipt
        self.date_of_completion = date_of_completion
        self.full_name = full_name
        self.status = status
        Receipt.count += 1

    @staticmethod
    def clients_new():
        name = input("Введите Ф.И.О")
        technics = input("Выберите, что ремонтируем:\n"
                         "1-Телефон\n"
                         "2-Нотбук\n"
                         "3-Телевизор\n")

        if technics == '1':
            tel = Telephone(Receipt.count, 'телефон', input("Марка телефона"),
                            input("Введите операционную систему"), input("Опишите поломку"),
                            date, date2, name, "ремонтируется")
            tel.conclusion()

        elif technics == '2':
            lap = Laptop(Receipt.count, 'ноутбук', input("Марка ноутбука"),
                         input("Введите операционную систему"), input("Дата выпуска"), input("Опишите поломку"),
                         date, date2, name, "ремонтируется")
            lap.conclusion()

        elif technics == '3':
            tv = Tv(Receipt.count, "телевизор", input("Введите марку телевизора"),
                    input("Введите диагональ экрана"), input("Опишите поломку"), date,
                    date2, name, "ремонтируется")
            tv.conclusion()

    @staticmethod
    def receipt_info():
        step2 = input("Поиск: 1-по номеру квитанции\n"
                      "2-по ФИО\n")
        if step2 == "1":
            z = int(input("Введите номер квитанции"))
            for m in clients:
                if z in m:
                    print(m)
                    break
            else:
                print("Клиент с такими данными отсутствует")
        if step2 == "2":
            z1 = input("Введите ФИО")
            for p in clients:
                if z1 in p:
                    print(p)


class Admin:
    def __init__(self, login, password, name):
        self.name = name
        self.password = password
        self.login = login
        k = [self.login, self.password, self.name]
        admin.append(k)

    @staticmethod
    def admin_action():
        login = input('Ведите логин администратора')
        password1 = input('Введите пароль')
        for v in admin:
            if login in v[0] and password1 in v[1]:
                print(f"Приветствую Вас: {v[2]}")
                choice = input("Выберите действие:\n"
                               "1-панель администратора\n"
                               "2-работа с квитанциями\n")
                if choice == '1':
                    arm = input("1-отобразить список всех админов\n"
                                "2-удалить админа из списка\n"
                                "3-добавить нового админа\n")
                    if arm == '1':
                        for b in admin:
                            print(b[2])
                    elif arm == '2':
                        for q in admin:
                            print(q[2])
                        all1 = input("Введите ФИО кого удалить")
                        for t in admin:
                            if all1 in t:
                                admin.remove(t)
                                print(admin)

                    elif arm == '3':
                        Admin(input("Введите логин администратора"), input("Введите пароль администратора"),
                              input("Введите Ф.И.О. администратора"))
                        print(admin)

                elif choice == '2':
                    z = int(input("Введите номер квитанции"))
                    for g in clients:
                        if z in g:
                            z1 = input("Выберете действие:\n"
                                       "1-изменить статус ремонта\n"
                                       "2-изменить дату выполнения ремонта\n"
                                       "3-посмотреть иформацию о квитанции\n")
                            if z1 == "1":
                                for y in clients:
                                    if z in y:
                                        y[-1] = input("Введите статус")
                                        print(y)

                            elif z1 == "2":
                                for w in clients:
                                    if z in w:
                                        w[6] = input("Введите дату завершения ремонта")
                                        print(w)

                            elif z1 == "3":
                                for e in clients:
                                    if z in e:
                                        print(e)
                            break
                    else:
                        print("Клиент с такими данными отсутствует")
                break
        else:
            print("Пользователь с таким логином и паролем отсутствует")


class Telephone(Receipt):
    def __init__(self, receipt_number, product_type, brand, operating_system, breaking,
                 date_of_receipt, date_of_completion, full_name, status):
        super().__init__(receipt_number, product_type, date_of_receipt, date_of_completion, full_name, status)
        self.brand = brand
        self.operating_system = operating_system
        self.breaking = breaking
        a = [self.receipt_number, self.product_type, self.brand, self.operating_system, self.breaking,
             self.date_of_receipt, self.date_of_completion, self.full_name, self.status]
        clients.append(a)

    def conclusion(self):
        print(
            f"Номер квитанции:{self.receipt_number}\n"
            f"Тип изделия:{self.product_type}\n"
            f"Марка телефона:{self.brand}\n"
            f"Операционная система :{self.operating_system}\n"
            f"Опиcание поломки :{self.breaking}\n"
            f"Дата приемки:{self.date_of_receipt}\n"
            f"Дата выполнения ремонта:{self.date_of_completion}\n"
            f"Ф.И.О:{self.full_name}\n"
            f"Статус:{self.status}\n"
        )


class Laptop(Receipt):

    def __init__(self, receipt_number, product_type, brand, operating_system, production_date, breaking,
                 date_of_receipt, date_of_completion, full_name, status):
        super().__init__(receipt_number, product_type, date_of_receipt, date_of_completion, full_name, status)
        self.production_date = production_date
        self.brand = brand
        self.operating_system = operating_system
        self.breaking = breaking
        b = [self.receipt_number, self.product_type, self.brand, self.operating_system, self.production_date,
             self.breaking, self.date_of_receipt, self.date_of_completion, self.full_name, self.status]
        clients.append(b)

    def conclusion(self):
        print(
            f"Номер квитанции:{self.receipt_number}\n"
            f"Тип изделия:{self.product_type}\n"
            f"Марка ноутбука:{self.brand}\n"
            f"Операционная система :{self.operating_system}\n"
            f"Год выпуска:{self.production_date}\n"
            f"Опиcание поломки :{self.breaking}\n"
            f"Дата приемки:{self.date_of_receipt}\n"
            f"Дата выполнения ремонта:{self.date_of_completion}\n"
            f"Ф.И.О:{self.full_name}\n"
            f"Статус:{self.status}\n"
        )


class Tv(Telephone):

    def conclusion(self):
        print(
            f"Номер квитанции:{self.receipt_number}\n"
            f"Тип изделия:{self.product_type}\n"
            f"Марка телевизора:{self.brand}\n"
            f"Диагональ экрана :{self.operating_system}\n"
            f"Опиcание поломки :{self.breaking}\n"
            f"Дата приемки:{self.date_of_receipt}\n"
            f"Дата выполнения ремонта:{self.date_of_completion}\n"
            f"Ф.И.О:{self.full_name}\n"
            f"Статус:{self.status}\n")


admin1 = Admin('11', '222', 'Семен Игоревич')
admin2 = Admin('seganik4', '654321R', 'Валерий Иванович')
admin3 = Admin('bugimen', '13579P', 'Галина Николаевна')

clients1 = Telephone(Receipt.count, 'телефон', 'samsung', 'андроид', 'разбит экран', '12.02.2022',
                     '17.02.2022', 'Андрей Белов', 'ремонт')
clients2 = Tv(Receipt.count, 'телевизор', 'LG', '52 дюйма', 'не включается', '12.02.2022', '17.02.2022',
              'Иван Усович', 'готово')
clients3 = Laptop(Receipt.count, 'ноутбук', 'acer', 'windows', '2019 год выпуска', 'не включается',
                  '12.02.2022', '17.02.2022', 'Гарик Харламов', 'ремонт')
clients4 = Telephone(Receipt.count, 'телефон', 'xiaomi', 'андроид', 'не заряжается', '12.02.2022',
                     '17.02.2022', 'Павел Воля', 'ремонт')
clients5 = Telephone(Receipt.count, 'телефон', 'apple', 'ios', 'зависает', '12.02.2022', '17.02.2022',
                     'Михаил Галустян', 'ремонт')
clients6 = Telephone(Receipt.count, 'телефон', 'xiaomi', 'андроид', 'не включается', '15.02.2022', '18.02.2022',
                     'Михаил Галустян', 'готов')

while True:
    step1 = input("Выберете действие:\n"
                  "1-Сдать в ремонт\n"
                  "2-Постмотреть информацию\n"
                  "3-Зайти в панель администратора\n")
    if step1 == '1':
        Receipt.clients_new()

    elif step1 == '2':
        Receipt.receipt_info()

    elif step1 == '3':
        Admin.admin_action()

    with open("file.txt", "w") as file:
        json.dump(clients, file)
    with open("file.txt", "r") as file:
        f = json.load(file)
        for i in f:
            print(i)
