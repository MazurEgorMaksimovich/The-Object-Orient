class Futboljor:
    """Создаёт футболиста, даёт ему имя и позицию."""

    def __init__(self, name, position):
        self.name = name
        self.position = position
        print("Я ---- " + self.name + ", играю как " + self.position + ".")
        print("\n")

def main():
    """Мэин, просто Мэин."""

    for i in range(11):
        name = (input("Как зовут игрока номер " + str(i+1) + "? "))
        print()
        if i == 0:
            position = "вратарь"
        elif 1 <= i <= 3:
            position = "защитник"
        elif 4 <= i <= 7:
            position = "полузащитник"
        else:
            position = "нападающий"
        player = Futboljor(name, position)

main()    