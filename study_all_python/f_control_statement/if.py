number = 15

if number % 3 == 0:
    print(f"{number}는 3의 배수이다")
if number % 5 == 0:
    print(f"{number}는 5의 배수이다")


# number가 양수인지 음수인지, 0 인지 검사

if number > 0:
    print(f"{number}는 양수입니다")

if number < 0:
    print(f"{number}는 음수입니다")

if number == 0:
    print(f"{number}는 0입니다")


#나이 입력 받기
# 미성년자인지 검사

age = int(input("나이를 입력하세요"))

if age > 19:
    print("성인입니다")
else: print("미성년자입니다")