from Animal import(
    Animal,
)

class Menu:
    '''Класс для работы пользовательского меню.'''

    def print_main_menu(self) -> None:
        '''Пункты пользовательского меню'''

        print(
            '\n1: Печать инфо о животном.\n'
            '2: Печать инфо об имени животного.\n'
            '3: Печать инфо о классе животного.\n'
            '4: Печать инфо о среднем весе животного.\n'
            '5: Измененение имени животного\n'
            '6: Изменение класса животного\n'
            '7: Изменение среднего веса животного\n'
            '8: Печать инфо о настроении животного\n'
            '9: Печать инфо о том, крупное, среднее или маленькое животное\n'
            '10: Погладить животное\n'
            '0: ВЫХОД ИЗ ПРОГРАММЫ!\n'
        )

    def main_menu(self, choise: int, animal: Animal) -> bool:
        '''Главное меню пользователя
        
        Args:
            choise: Выбор пользователя

        Returns:
            is_running: Работает ли еще программа
        '''

        is_running = True

        match choise:
            case 0:
                is_running = False
            case 1:
                animal.info()
            case 2:
                print(animal.get_name())
            case 3:
                print(animal.get_species())
            case 4:
                print(animal.get_average_weight())
            case 5:
                name = input("Введите имя животного")

                animal.set_name(name)
            case 6:
                species = input("Введите класс животного")

                animal.set_species(species)
            case 7:
                average_weight = input("Введите имя животного")

                animal.set_average_weight(average_weight)
            case 8:
                f'{"Хорошее настроение" if self.get_mood() else "Плохое настроение"}'
            case 9:
                animal.get_size_category()
            case 10:
                animal.pet()

                
        
        return is_running
            
