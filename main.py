"""Имя файла записано в константу NAME_FILE"""

from typing import Final

NAME_FILE: Final[str] = 'database.txt'


def write_file(login: str, password: str) -> None:
    """
    Запись в файл.

    Открываем файл на запись и записываем в файл.

    Args:
        login: str (первый аргумент, логин)
        password: str (второй аргумент, пароль)
    """
    with open(NAME_FILE, 'a+', encoding='utf-8') as file:
        file.write(f'{login} {password}\n')


def read_file() -> str:
    """
    Читаем из файла.

    Открываем файл и читаем данные из файла.

    Returns:
        str: Возвращаем результат чтения данных из файла
    """
    with open(NAME_FILE, 'r', encoding='utf-8') as file:
        return file.read()


def registration() -> None:
    """
    Регистрация нового пользователя.

    Делаем проверки перед регистрацией для нового пользователя
    """
    try:
        new_login = input('придумайте логин: ')
        new_password = input('придумайте пароль: ')
        lst_database = read_file().split('\n')
        gen_lst_database = \
            [list(i.split(' ')) for i in lst_database if i != '']
        dict_database = dict(gen_lst_database)
        if new_login in dict_database.keys():
            print('\nлогин существует, повторите попытку!\n')
        else:
            if 3 <= len(new_login) <= 20 and 4 <= len(new_password) <= 32:
                write_file(new_login, new_password)
                print('\nрегистрация прошла успешно!\n')
            else:
                print('\nневерное колличество символов логина или пароля, '
                      'повторите попытку!\n')
    except FileNotFoundError:
        print(f'\nзапрашиваемый файл {NAME_FILE} не найден, '
              f'проверьте путь к файлу!\n')


def authorization() -> None:
    """
    Авторизация пользователя.

    Выполнение проверок перед авторизацией для подтверждения пользователя.
    """
    try:
        user_login = input('введите ваш логин: ')
        user_password = input('ведите ваш пароль: ')
        lst_database = read_file().split('\n')
        gen_lst_database = \
            [list(i.split(' ')) for i in lst_database if i != '']
        dict_database = dict(gen_lst_database)
        if (user_login in dict_database.keys()
                and dict_database[user_login] == user_password):
            print('\nавторизация прошла успешно!\n')
        else:
            print('\nлогин или пароль не существует, '
                  'повторите попытку!\n')
    except FileNotFoundError:
        print(f'\nзапрашиваемый файл {NAME_FILE} не найден, '
              f'проверьте путь к файлу!\n')


def main(action: str) -> None:
    """
    Выбор действия.

    Запрашивывает и выбирает соответствующие действия.

    Args:
        action: str (принимает строку, наименование действия)
    """
    if action == '1':
        registration()
    elif action == '2':
        authorization()
    else:
        print('\nвведённого действия не существует, повторите попытку!\n')


if __name__ == '__main__':
    user_name = input('ведите ваше имя: ')
    print(f'здравствуйте, {user_name}!')
    main(input('выберете ваше действие, '
               '1 - регистрация или 2 - авторизация: '))