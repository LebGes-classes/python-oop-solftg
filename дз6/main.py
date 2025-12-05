from Animal import(
    Animal,
)
from menu import(
    Menu,
)

menu = Menu()
animal_1 = Animal()
animal_2 = Animal("Гепард", "Млекопитающее", "50")

def run() -> None:
    '''Метод запуска работы.'''

    is_running = True

    while(is_running):

        menu.print_main_menu()

        choise = int(input("Введите выбор: "))
        choise_animal = int(input("Введите номер животного: "))
        animal = animal_1 if choise_animal == 1 else animal_2

        is_running = menu.main_menu(choise, animal)


run()