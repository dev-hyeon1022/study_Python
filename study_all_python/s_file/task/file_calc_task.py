# 두 정수의 연산을 수행하는 계산기 모듈 제작
# 연산 수행 시 해당 시간을 기록하고,
# 연산 수행 중 오류 발생 시 오류 사항과 시간을 기록하도록 한다.

# 입력 예
# 두 정수를 입력하세요.
# 연산자를 선택하세요

# 출력 예
# 1 + 3 = 4
# 10 / 0 = ZeroDivisionError

import datetime



def calculator():

    def add(num1, num2):
        return num1 + num2

    def min(num1, num2):
        return num1 - num2

    def mul(num1, num2):
        return num1 * num2

    def div(num1, num2):
        return num1 / num2
    return {"+": add, "-": min, "*": mul, "/":div}


def log_now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def log_file(textmessage):
    file = open("logs.txt", "a", encoding="utf-8")
    print(log_now())
    file.write(textmessage)


num_input_message = "두 정수를 입력하시오"
operator_choice_input_message = "연산자를 선택하세요\n1.더하기\n2.빼기\n3.곱하기\n4.나누기\n5.나가기\n"
operator_choice_input_error_message = "1 ~ 5 값을 입력하시오"


while True:
    num1, num2 = input(num_input_message).split()
    num1 = int(num1)
    num2 = int(num2)
    operator_num = int(input(operator_choice_input_message))

    try:
        if operator_num == 1:
            print(calculator()["+"](num1, num2))


        elif operator_num == 2:
            print(log_now())
            calculator()["-"](num1, num2)


        elif operator_num == 3:
            calculator()["*"](num1, num2)
            print(log_now())


        elif operator_num == 4:
            calculator()["/"](num1, num2)


        elif operator_num == 5:
            break
        else:
            print()

    except ZeroDivisionError:
        str = f"\n{num1} / {num2} = ZeroDivisionError\n"
        print(str)

        file = open("logs.txt", "a", encoding="utf-8")
        file.write(log_now())
        file.write(str)
        file.close()

    except Exception:
        file = open("logs.txt", "a", encoding="utf-8")
        file.write(date + "\n알 수 없는 오류\n")
        file.close()





