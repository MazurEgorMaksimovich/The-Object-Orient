class TeleVision:
    """Имитатор телика."""

    def __init__(self, tek_kan = 1, tek_gromk = 20):
        self.__tek_kan = tek_kan
        self.__tek_gromk = tek_gromk
    
    def kan_perek(self, vektor):
        """Переключает каналы."""

        if vektor == "1":
            self.__tek_kan -= 1
            if self.__tek_kan < 1:
                self.__tek_kan = 69
        elif vektor == "2":
            self.__tek_kan += 1
            if self.__tek_kan > 69:
                self.__tek_kan = 1
        print("Текущий канал: " + str(self.__tek_kan) + ".")
    
    def gromk_izm(self, vektor):
        """Изменяет громкость."""

        if vektor == "3":
            self.__tek_gromk -= 1
            if self.__tek_gromk < 0:
                self.__tek_gromk = 0
        elif vektor == "4":
            self.__tek_gromk += 1
            if self.__tek_gromk > 100:
                self.__tek_gromk = 100
        print("Текущая громкость: " + str(self.__tek_gromk) + ".")

def main():
    """Мэин, Просто Мэин"""
    
    telik = TeleVision()

    choice = None
    while choice != "0":
        print \
            ("""
            Вы смотрите Телевизор, созданный компанией "Тэ-Вэ Боги".

            0 - Выключить телик.
            1 - Переключить канал на один меньше.
            2 - Переключить канал на один больше.
            3 - Уменьшить громкость на один.
            4 - Увеличить громкость на один.
            """)
        
        choice = input("Ваш выбор: ")
        print()

        if choice == "0":
            print("До свидание.")
        elif choice == "1" or choice == "2":
            telik.kan_perek(choice)
        elif choice == "3" or choice == "4":
            telik.gromk_izm(choice)
        else:
            print("Извините, в меню нет пункта", choice)

main()