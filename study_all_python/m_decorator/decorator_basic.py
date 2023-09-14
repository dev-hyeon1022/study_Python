def 데코레이터이름(원래함수):
    def 주변로직(원래함수가받은거):
        완성코드 = 원래함수가받은거 + "님"
        원래함수(완성코드)

    return 주변로직


@데코레이터이름
def 원래함수(이름):
    print(이름)


원래함수('한동석')

# 나이를 전달받은 뒤 나이 뒤에 '살'을 붙여 출력

def add_decorato(print_age):
    def add_sal(print_age):
        print_sal = print_age + "살"
        print_age(print_sal)

    return add_sal



@add_decorato
def print_age(age):
    print(age)

print_age(10)
