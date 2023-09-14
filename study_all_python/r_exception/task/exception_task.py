# 캐릭터 닉네임 정할 때 비속어를 사용하지 못하게 막아주기
# 바보 멍게 해삼 운영자
# 직접 Error를 제작하여 발생 시 안내 메세지까지 출력하기

class SetNameFilterError(Exception):
    def __str__(self):
        return "바보 멍게 해삼 운영자 포함된 닉네임은 불가능합니다"


def check_set_nickname(nickname):
    if nickname.__contains__("바보"):
        raise SetNameFilterError
    elif nickname.__contains__("멍게"):
        raise SetNameFilterError
    elif nickname.__contains__("해삼"):
        raise SetNameFilterError
    elif nickname.__contains__("운영자"):
        raise SetNameFilterError


try:
    name = input("닉네임: ")
    check_set_nickname(name)
    print(name)
except SetNameFilterError as e:
    print(e)







