# 국어, 영어, 수학 점수를 전달받은 뒤 총 점을 출력하는 함수
# list에 국어, 영어, 수학 점수를 각각 담은 후 unpacking 발생시키기

def age_unpacking(kr, en, math):
    return kr + en + math

mylist = [70,80,90]

print(age_unpacking(*mylist))


# 문자열에서 'A'가 몇 개 있는 지 검사하는 함수
#packing
def check_A_packing(*str):
    result = 0
    for i in str:
        result += i.count("A")

    return result


data = "Apple", "Animal","banna","AAAAAA","AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
print(check_A_packing(*data))
