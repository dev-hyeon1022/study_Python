# 동물
# 이름, 나이, 성별

class Animal:
        def __init__(self, name, age, gender):
            self.name = name
            self.age = age
            self.gender = gender
            self.food = 10
            self.heart = 10
            print(f"이름:{self.name} 나이:{self.age} 성별:{self.gender}")

        def eat(self):
            self.food -= 1
            print(f"음식 1개 소진 남은 음식:{self.food}")

        def moveing(self):
            self.food += 1
            self.heart -= 1
            print(f"음식 1개 획득, 체력 1개 소진\n남은 음식:{self.food}, 남은 체력:{self.heart}")


dog = Animal("뽀삐",2,"암컷")

dog.eat()
dog.eat()
dog.eat()
dog.eat()
dog.moveing()

