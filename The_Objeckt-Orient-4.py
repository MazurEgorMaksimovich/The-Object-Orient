import random

class Pet:
    """Виртуальный питомец"""
    total = 0

    @staticmethod
    def status():
        print('Общее число зверюшек', Pet.total)

    def __init__(self, name, hunger, bordom):
        self.__name= name
        self.hunger = hunger
        self.bordom = bordom
        Pet.total += 1
        print("***Однажды, на Луне родилась необычная зверюшка***")
        print("Я родился!!!")
        print("Привет. Я ---- зверюшка " + self.__name + ".")
        print()

    def talk(self):
        """Разговоры со зверюшкой"""

        print("Меня зовут", self.__name, "и сейчас я чувствую себя", self.mood)
        print()
        self.__pass_time()
    
    def __str__(self):
        ans = "Объект класса Pet \n"
        ans += "Имя ---- " + self.name + "\n"
        return ans

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Не будь зверем! Дай зверюшке имя!")
        else:
            self.__name = new_name
            print("Имя успешно изменено")
    
    @property
    def mood(self):
        """Рассказывает о самочувствии зверюшки"""
        unhappiness = self.hunger + self.bordom
        if unhappiness < 5:
            m = 'прекрасно!'
        elif 5 <= unhappiness <= 10:
            m = 'норм.'
        elif 11 <= unhappiness <= 15:
            m = 'не то, чтобы хорошо.'
        else:
            m = 'ужасно!'
        return m
    
    def __pass_time(self):
        """Мотает время"""
        self.hunger += 1
        self.bordom += 1

    def eat(self):
        """Позволяет покормить зверюшку"""
        food = int(input("Сколько еды получит зверюшка? "))
        print("Мммм... Как вкусно...")
        print()
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time

    def play(self):
        """Позволяет поиграть со зверюшкой"""
        fun = int(input("Сколько времени вы потратите на игру со зверюшкой? "))
        print("Уиии... Я умею летать!!!")
        print()
        self.bordom -= fun
        if self.bordom < 0:
            self.bordom = 0
        self.__pass_time

def main():
    """Мэин, Просто Мэин"""

    pets = []

    pets_kol = int(input("Сколько зверюшек планируете завести? "))
    for _ in range(pets_kol):
        pet_name = input("Как вы назовёте зверюшку №" + str(_+1) + "? ")
        print()
        pet_hunger = random.randint(0, 11)
        pet_bordom = random.randint(0, 11)
        pet = Pet(pet_name, pet_hunger, pet_bordom)
        pets.append(pet)

    choice = None
    while choice != "0":
        print \
            ("""
            Зооферма

            0 - Выйти
            1 - Узнать о самочувствии зверюшек
            2 - Покормить зверюшек
            3 - Поиграть со зверюшками
            """)
        
        choice = input("Ваш выбор: ")
        print()

        if choice == "0":
            print("До свидание.")
        elif choice == "1":
            for pet in pets:
                pet.talk()
        elif choice == "2":
            for pet in pets:
                pet.eat()
        elif choice == "3":
            for pet in pets:
                pet.play()
        else:
            print("Извините, в меню нет пункта", choice)

main()