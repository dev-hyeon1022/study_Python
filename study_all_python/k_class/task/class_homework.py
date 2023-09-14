# 1
class Animals:
    count = 0

    def __init__(self, name, age, gender, food=0, health=0):
        self.name = name
        self.age = age
        self.gender = gender
        self.health = health
        self.food = food
        self.maxfood = food
        self.maxhealth = health
        Animals.count += 1

    def animal_info(self):
        print(f"이름: {self.name}\n나이: {self.age}\n성별: {self.gender}")
        print(f"총 동물 수:{Animals.count}")

    def eat(self):
        if 0 < self.food <= self.maxfood: self.food -= 1
        if 0 < self.health < self.maxhealth: self.health += 1
        print(f"간식 -1 | 체력 +1")
        print(f"간식:{self.food}/{self.maxfood} 체력:{self.health}/{self.maxhealth}\n")

    def training(self):
        if 0 < self.food < self.maxfood: self.food += 1
        if 0 < self.health <= self.maxhealth: self.health -= 1
        print(f"간식 +1 | 체력 -1")
        print(f"간식:{self.food}/{self.maxfood} 체력:{self.health}/{self.maxhealth}\n")


# 2
class Drink:
    count = 0

    def __init__(self, name, ingredient, select_ice_or_hot):
        self.name = name
        self.ingredient = ingredient
        self.select_ice_or_hot = select_ice_or_hot

    def drink_info(self):
        print(f"총 만든 음료: {Drink.count}")

    def make_drink(self):
        if self.ingredient == "복숭아":
            if self.select_ice_or_hot == "ice":
                print(f"음료 제작 성공!: {self.name}")
                Drink.count += 1
            elif self.select_ice_or_hot == "hot":
                print(f"음료 제작 성공!: {self.name}")
                Drink.count += 1
            else:
                print("ice or hot 둘중 선택하시오")

        elif self.ingredient == "커피":
            if self.select_ice_or_hot == "ice":
                print(f"음료 제작 성공!: {self.name}")
                Drink.count += 1
            elif self.select_ice_or_hot == "hot":
                print(f"음료 제작 성공!: {self.name}")
                Drink.count += 1
            else:
                print("ice or hot 둘중 선택하시오")

        elif self.ingredient == "초코":
            if self.select_ice_or_hot == "ice":
                print(f"음료 제작 성공!: {self.name}")
                Drink.count += 1
            elif self.select_ice_or_hot == "hot":
                print(f"음료 제작 성공!: {self.name}")
                Drink.count += 1
            else:
                print("ice or hot 둘중 선택하시오")

        else:
            print("제작에 필요한 레시피가 없습니다")


# 3
class Car:
    def __init__(self, name, color, size, wheel=4):
        self.name = name
        self.color = color
        self.size = size
        self.wheel = wheel

    def custom_car(self):
        print(f"이름: {self.name}\n색상: {self.color}\n사이즈: {self.size}")


# 4
class Bedding:
    def __init__(self, now_season):
        self.now_season = now_season

    def recommend_bedding(self):
         if self.now_season == "봄": print("선선한 이불 추천!")
         elif self.now_season == "여름": print("얇고 시원한 이불 추천!")
         elif self.now_season == "가을": print("부드러운 이불 추천!")
         elif self.now_season == "겨울": print("따듯한 이불 추천!")
         else:print("봄, 여름, 가을, 겨울 중 입력해주세요")


# 5
class Rides:
    def __init__(self, rides_name, size):
        self.rides_name = rides_name
        self.size = size

    def riding(self):
        if self.rides_name == "롤러코스터":
             if self.size >= 150:
                 print("롤러코스터 탑승!")
             else: print("150cm 미만 탑승불가!")

        elif self.rides_name == "바이킹":
             if self.size >= 130:
                 print("바이킹 탑승!")
             else: print("130cm 미만 탑승불가!")

        elif self.rides_name == "후룸라이드":
             if self.size >= 150:
                 print("후룸라이드 탑승!")
             else: print("150cm 미만 탑승불가!")
        else:print("해당 놀이기구가 없습니다")


# 6
class Rental_car:
    def __init__(self, rental_car_name, age, is_license):
        self.rental_car_name = rental_car_name
        self.age = age
        self.is_license = is_license

    def rental_car(self):
        if self.age >= 20:
            if self.is_license:
                print(f"{self.rental_car_name}렌트완료!")
            else: print("면허증 없음으로 렌트 안됨")
        else: print("나이가 20세 미만으로 렌트 안됨")


# 7
class Office_workers:
    def __init__(self, job, age, workspace, salary):
        self.job = job
        self.age = age
        self.workspace = workspace
        self.salary = salary

    def worker_info(self):
        print(f"직업: {self.job} 나이: {self.age} 근무지:{self.workspace} 연봉: {self.salary}")


# 8
class Guitar:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def buy(self):
        print(f"{self.name} - {self.price} 구입완료!")


    def sell(self):
        print(f"{self.name} - {self.price} 판매완료!")


# 9
class Soccer:
    def __init__(self, name, number, pos):
        self.name = name
        self.number = number
        self.pos = pos


    def info(self):
        print(f"이름: {self.name} 번호: {self.number} 포지션: {self.pos}")

    def shooting(self):
        print(f"{self.name} 선수가 슛우웃~!")

    def dribble(self):
        print(f"{self.name} 선수의 화려한 드리블!")


# 10
class Mountain:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def climb(self):
        print(f"산:{self.name} 해발:{self.height} 오르다")

    def descend(self):
        print(f"산:{self.name} 해발:{self.height} 하산하다")


# 11
class Monster:
    def __init__(self, name, hp, attack, speed):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.speed = speed


    def move(self):
        print(f"{self.speed}의 속도만큼 움직인다")

    def monster_attack(self):
        print(f"{self.attack}의 만큼 공격한다")

    def monster_heal(self):
        print("1의 만큼 회복한다")
        print(f"현재 체력:{self.hp}")


# 12
class Shoes:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def try_on_shoes(self):
        if  self.size == 270: print("사이즈가 딱 맞습니다")
        else:print("사이즈가 맞지 않습니다")


# 13
class Notebook:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def find_of_notebook(self):
        if self.brand == "삼성":
            if self.color == "흰색":
                print(f"{self.color} {self.brand}노트북!")
            elif self.color == "검은색":
                print(f"{self.color} {self.brand}노트북!")
            else:print("흰색 or 검은색 중 입력하시오")

        elif self.brand == "엘지":
            if self.color == "흰색":
                print(f"{self.color} {self.brand}노트북!")
            elif self.color == "검은색":
                print(f"{self.color} {self.brand}노트북!")
            else:print("흰색 or 검은색 중 입력하시오")

        else:print("삼성 or 엘지 중 입력하시오")


# 14
class Pizza:
    count = 0
    def __init__(self, name, ingredient):
        self.name = name
        self.ingredient = ingredient

    def pizza_info(self):
        print(f"총 만든 피자: {Pizza.count}")

    def make_pizza(self):
        if self.ingredient == "고구마":
            print(f"피자 제작 성공!: {self.name}")
            Pizza.count += 1
        elif self.ingredient == "포테이토":
            print(f"피자 제작 성공!: {self.name}")
            Pizza.count += 1
        else:
            print("제작에 필요한 레시피가 없습니다")


# 15
class Game:
    def __init__(self,pc_or_console):
        self.pc_or_console = pc_or_console

    def get_game_type(self):
        if self.pc_or_console == "pc": print("PC 게임입니다")
        elif self.pc_or_console == "console": print("Console 게임입니다")


# 16
class Movie:
    def __init__(self, movie_name):
        self.movie_name = movie_name

    def showing_movie(self):
        if self.movie_name == "범죄도시3":
            print("현재 상영중인 영화입니다")
        elif self.movie_name == "엘리멘탈":
            print("현재 상영중인 영화입니다")
        else: print("준비중입니다")


# 17
class Picture:
    def __init__(self, drawing_paper):
        self.drawing_paper = drawing_paper

    def draw(self):
        print(f"{self.drawing_paper}에 그림그리기")

    def delete_picture(self):
        print("그림 삭제!")

# 18
class Login:
    def __init__(self, id, password):
        self.id = id
        self.password = password

    def login(self):
        if self.id == "ok123" and self.password == "1234": print("로그인 성공")
        else:print("로그인 실패")


#19
class Phone:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def find_of_phone(self):
        if self.brand == "삼성":
            if self.color == "흰색":
                print(f"{self.color} {self.brand}핸드폰!")
            elif self.color == "검은색":
                print(f"{self.color} {self.brand}핸드폰!")
            else:
                print("흰색 or 검은색 중 입력하시오")

        elif self.brand == "애플":
            if self.color == "흰색":
                print(f"{self.color} {self.brand}핸드폰!")
            elif self.color == "검은색":
                print(f"{self.color} {self.brand}핸드폰!")
            else:
                print("흰색 or 검은색 중 입력하시오")

        else:
            print("삼성 or 애플 중 입력하시오")


# 20
class Television:
    def __init__(self, volume, channel, is_on):
        self.volume = volume
        self.channel = channel
        self.is_on = is_on

    def power_on_off(self):
        if self.is_on == "true":
            self.is_on = "false"
        elif self.is_on == "false":
            self.is_on = "true"
        else: print("true false 중 입력하시오")

    def up_volume(self):
        self.volume +=1
        print(f"현재 볼륨{self.volume}")

    def down_volume(self):
        self.volume -=1
        print(f"현재 볼륨{self.volume}")


    def up_channel(self):
        self.channel +=1
        print(f"현재 볼륨{self.channel}")

    def down_channel(self):
        self.channel -=1
        print(f"현재 볼륨{self.channel}")





