def add(x, y):
    return x + y

# 람다(lambda): 이름이 없는 함수, 일회성, 매개변수 혹은 리턴값에 작성 가능
# lambda 매개변수,...: 리턴값

add = lambda x, y: x + y
result = add(1, 2)
print(result)

# map(function, iterator)
datas = [1, 2, 3, 4, 5]
# result = []

# for i in datas:
#     result.append(i * 2)
#
# print(result)

# 함수를 lambda 함수로 사용하는데 선언시 (lambda 매개 변수:리턴값) 이런식으로 사용한다
# 이때 mpa 함수는 (함수,순서가 있는 값 ex)list)이렇게 사용하고
# 지금은 lambda 함수에 number라는 매개변수를 받고 받은 number매개변수를 곱하기 2로 리턴해주는데
# 각각의 datas의 값에 곱하기 2를 해서 나온 값을 list로 형변환 시켜 출력하는 코드이다

print(list(map(lambda number: number * 2, datas)))

for i in map(lambda number: number * 2, datas):
    print(i)


# 경로(/a, /b, ..) 앞에 /app 연결시키기
urls = ['/game', '/news', '/fashion', '/ranking']


real_urls = list(map(lambda url: f'/app{url}', urls))
print(real_urls)


# filter(function, iterator)
# '/app/game'.split("/")[-1] == 'game'
print(list(filter(lambda url: url.split("/")[-1] == 'game', real_urls)))


# 1 ~ 10까지 중 짝수만 추출
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda num: num % 2 == 0, numbers)))

print(list(filter(lambda num: num % 2 == 0, [i + 1 for i in range(10)])))


