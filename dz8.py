# Задача №49. Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
contact_data = {
    'ferst_name': None,
    'second_name': None,
    'phone_number': None
}


def ask_data():
    f_name = input("Введите имя: ")
    m_name = input("Введите отчество: ")
    s_name = input("Введите фамилию: ")
    phone = input("Введите номер телефона: ")
    contact = {'ferst_name': f_name,
        'middle_name': m_name,
        'second_name': s_name,
        'phone_number': phone}
    return contact

def add_new_contact():
    contact = ask_data()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        for value in contact.values():
            file.write(f"{value}; ")
        file.write('\n')
    return True

def open_phonebook():
    title = ["Фамилия", "Имя", "Отчество", "Телефон"]
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print("\t\t".join(title))
        for line in file:
            print("\t\t".join(line.split(";")))

def find_contact():
    title = ["Фамилия", "Имя", "Отчество", "Телефон"]
    print(f'Поиск по:\n1 Имени\n2 Фамилии\n3 Отчеству\n4 Телефону\n0 выход')
    s_name = input("Введите фамилию: ")
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print("\t\t".join(title))
        for line in file:
            line = line.split()
            if s_name in line[0]:
                print("\t\t".join(line))

def main():
    isStop = 10
    while isStop != 0:
        print(f'Выберете что хотите сделать:\n1 посмотреть\n2 добавить\n3 сохранить\n4 открыть\n5 копировать\n0 выход')
        isStop = int(input(">"))
        if isStop == 1:
            find_contact()
        elif isStop == 2:
            add_new_contact()
        elif isStop == 4:
            open_phonebook()
        input('Нажмите Enter чтобы продолжить')


main()
