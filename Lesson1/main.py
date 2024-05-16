name = input('Enter your name\n')

age = input('How old are you\n')

favouriteGame = input('Your favourite computer game\n')


# Создаем функцию 
def spaceInsert(_a ,_b, _c):
    if _c== "Dota 2":
        return _a + " " + _b + " " + _c + " no gf" 
    return _a + " " + _b + " " + _c + " probably has gf"


#print(spaceInsert(name,age, favouriteGame))


#Создаем класс
class Anketa:
    #Создаем конструктор
    def __init__(self, name, age, game):
        self.game = game
        self.name = name
        self.age = age
        
    #Создаем функцию
    def print(self):
        print(self.game+"")
        print(self.name+"")
        print(self.age+"")
#Вызываем конструктор
person = Anketa(name = name, age = age, game= favouriteGame)

#Вызываем метод print у объекта print()
person.print()

person  = Anketa(name="Vadim",  age = "20", game = "CS2")

person.print()