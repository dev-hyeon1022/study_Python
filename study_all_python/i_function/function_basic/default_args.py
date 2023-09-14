# 만약 값을 매개변수로 전달하지 않았을 경우
# 기본 값을 설정하기 위해서는 arg=default_value로 설정한다


# sub 라는 함수를 매개변수 number1~4까지 선언하고
#사용자가 최대 매개변수보다 적게 사용시 ★뒤에서부터★ 기본값 으로 설정한 number4이다
# 따라서 number4의 값은 0이다
def sub(number1, number2, number3, number4=0):
    return number1 - number2 - number3 - number4


result = sub(1, 2, 3)
print(result)


# 위 설명과 같이 매개변수를 기본값으로 설정하고
# 만약 사용자가 매개변수를 대입하지 않고 get_info()이대로 사용시
# name 값은 '익명'| age 값은 0
# 밑에 사용자가 매개변수를 대입했으므로 따라서 출력은 '한동석', 20 으로 출력된다
def get_info(name='익명', age=0):
    return {"name": name, "age": age}


print(get_info('한동석', 20))