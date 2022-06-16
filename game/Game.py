from csv import writer

# file_object = open("Heroes_1.txt", encoding="UTF-8")
# file_content = file_object.read()
# file_object.close()
# file_object = open("Heroes_1.txt", "w" , encoding="UTF-8")



# weapons = ("Посох", "Меч", "Топор", "Лук", "Арбалет", "Щит")
# bronya = ("Кожа", "Латы", "Ткань", "Кольчуга")


hello = "Приветствую тебя Герой!\n Сейчас начнется твое приключение, но сперва надо выяснить кто ты есть по жизни. \n Выбери себе Имя, Класс(воин, маг, стрелок), так же укажи свой пол и возраст."
start_1 = "путешествие начинается!!!"



class Hero:

    def __init__(self, name, female, klass, age):
        self.name = name 
        self.female = female
        self.klass = klass
        self.age = age
        self.weapon = "Палка"
        self.hp = "1800"
        self.mp = "2500"
        self.eleksir = "5"
        self.shmot = "Броня 1-ого уровня"
        
        if self.klass == "воин":
            self.weapon = "Топор"
        elif self.klass == "стрелок":
            self.weapon = "Лук"
        elif self.klass == "маг":
            self.weapon = "Посох"

        
        if self.weapon == "Посох":
            self.hp = "1000"
            self.mp = "2500"
        elif self.weapon == "Лук":
            self.hp = "2000"
            self.mp = "100"
        else:
            self.hp = "3000"
            self.mp = "0"

    def personag(self):
        print("Итого вы\n" + self.name + "\n" + self.female + "\n" + "Великий " + self.klass + "\n" + self.age + " лет")
        print("Инвентарь \n" + self.hp + " ваше здоровье\n" + self.mp + " выша мана\n" + self.eleksir + " Элексиров\n" + self.shmot + "\n" + self.weapon + " ваше оружие") 
        


print(hello)
heroes_1 = Hero(input("введите имя персоонажа\n"), input("введите пол персоонажа\n"), input("введите класс персоонажа\n"), input("введите возраст персоонажа\n"))
print(heroes_1.personag())
print(heroes_1.name, start_1)



# file_object.write(file_content + "\n" + heroes_1.name + "\n" + heroes_1.female + "\n" + heroes_1.klass + "\n" + heroes_1.age)
# file_object.close()

# print("Итого вы\n" + heroes_1.name + "\n" + heroes_1.female + "\n" + "Великий " + heroes_1.klass + "\n" + heroes_1.age + " лет")
