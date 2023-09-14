# packing과 unpacking
# 함수 선언 시 매개변수에 한 번에 받을 것인지(packing)
# 따로 따로 분리해서 받을 것인지(unpacking)를 선택할 수 있다.

# unpacking
# 매개변수: a, b, c
# 사용 시: (*datas)

# packing
# 매개변수: *args(가변인자)
# 사용 시: (*datas)


# sub 함수가 매개변수 number1~3을 받고 3개의 값을 빼서 리턴해주는 함수이다
# 밑에 사용할때 data(tuple) 로 데이터를 받고 sub 호출시 그냥 sub(data)으로 넣으면
# 매개변수 number1에만 값이 들어가기 때문에 앞에 * 붙쳐서 각각의 매개변수에 대응해서 값이 들어간다

def sub(number1, number2, number3):
    return number1 - number2 - number3


data = 1, 2, 3

# unpacking
result = sub(*data)
print(result)

# sub 함수가 가변인자로 값을 받고 result 선언후
# for문으로 in 뒤에 순서가있는걸 리스트형변환 시켜줘서
# (args)가변인자를 i에다 받은 인자 값을 하나씩 대입해서 각각의 i값을
# 마이너스로 result에 누적시킨다 밑에 datas 에는 1, 2, 3의 tuple타입의 값이 있고
# sub 함수 호출시 앞에 *붙쳐서 -> sub(*datas) 값을 packing시켜 한번에 함수의 가변인자로 넘겨준다

# sub(
def sub(*args):
    result = 0
    for i in args:
        result -= i
    return result


datas = 1, 2, 3
# packing
print(sub(*datas))

# n개 정수의 합
# 매개변수의 개수를 알 수 없을 때에는 가변인자(*args)로 선언한다.
# 가변인자는 Tuple 타입이며, 전달할 대에는 ,로 여러 개의 값을 전달할 수 있다.


# packing
def getTotal(*numbers):
    total = 0
    for i in numbers:
        total += i

    return total


datas = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

result = getTotal(*datas)
# print(result)

# unpacking
# def getTotal(number1, number2, number3):
#     return number1 + number2 + number3
#
#
# datas = 1, 2, 3
# result = getTotal(*datas)
# print(result)


