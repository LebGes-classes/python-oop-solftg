class Animal:
    '''Класс для описания животных'''

    __mood = False

    def __init__(self, name: str = "NA", species: str = "NA", average_weight: int = "NA") -> None:
        '''Инициализация конструктора класса
        
        Args:
            name: имя животного
            species: класс животного
            average_weight: средний вес животного
        '''

        self.__name = name
        self.__species = species
        self.__average_weight = average_weight

    def set_name(self, name: str) -> None:
        '''Сеттер для имени животного
            
        Args:
            name: имя животного
        '''

        self.__name = name

    def get_name(self) -> str:
        '''Геттер для имени животного
            
        Returns:
            name: имя животного
        '''

        return self.__name

    def set_species(self, species: str) -> None:
        '''Сеттер для класса животного
            
        Args:
            species: класс животного
            '''

        self.__species = species

    def get_species(self) -> str:
        '''Геттер для класса животного
            
        Returns:
            species: клас животного
        '''

        return self.__species

    def set_average_weight(self, average_weight: int) -> None:
        '''Сеттер для среднего веса животного

        Args:
            average_weight: средний вес животного
        '''

        while(average_weight <= 0):
            average_weight = int(input("Введите корректный средний вес(покраинемере большt 0): "))

        self.__average_weight = average_weight

    def get_average_weight(self) -> int:
        '''Геттер для среднего веса животного животного
            
        Returns:
            average_weight: средний вес животного 
        '''
            
        return self.__average_weight
        
    def get_size_category(self, average_weight: int) -> str:
        '''Геттер для получения инфо о том к какой категории относится животное
            
         Args:
              average_weight: средний вес животного
        '''

        weight = self.__average_weight

        if weight <= 5:

            return "Маленькие"
        elif 5 < weight <= 50:

            return "Средние"
            
        return "Крупные"
    
    def info(self) -> None:
        '''Вывод информации о животном.'''

        print(
            f'\nИмя животного: {self.__name}\n'
            f'Класс животного: {self.__species}\n'
            f'Средний вес животного: {self.__average_weight}\n'
            f'{"Хорошее настроение" if self.get_mood() else "Плохое настроение"}\n'
        )

    def get_mood(self) -> bool:
        '''Геттер для настроения
        
        Returns __mood: настроение
        '''

        return self.__mood
    
    def pet(self) -> str:
        '''Функция для поглаживания животного
        
        Returns:
            __mood: настроение животного
        '''

        if self.__mood is False:
            self.__mood = True
            print("Вы погладили животное")
        
        return self.__mood