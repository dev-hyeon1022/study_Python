# Comprehension(컴프리헨션: 이해력)
# 반복되거나 특정 조건을 만족하는 리스트를 보다 쉽게 만들어 내기 위한 방법

# List Comprehension 구문
# [표현식 for 항목 in interator (if 조건)]

a = [1, 2, 3, 4]
# [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# print(a * 3)

# result = []

# for num in a:
#     result.append(num * 3)
#
# print(result)

result = [num * 3 for num in a]
print(result)

# [1, 2, 3, 4]
a = [1, 2, 3, 4]
# [6, 12]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

# [표현식 if 조건 else 표현식 for 항목 in interator (if 조건)]
# [1, 6, 3, 12]
a = [1, 2, 3, 4]
result = [num * 3 if num % 2 == 0 else num for num in a]
print(result)


a = [10, 20, 30, -20, -3, 50, -70]
# 위 리스트에서 '양수'만 추출하여 새로운 리스트 만들기

box = [num for num in a if num > 0]
print(box)


# # n개의 0으로만 채워진 list
n = int(input("숫자를 입력하시오: "))
box = [0 for i in range(n)]

print(box)

# 제곱의 결과가 10보다 큰 숫자를 담은 list
a = [1, -2, 3, -4, 5]
box = [i ** 2 for i in a if i ** 2 > 10]
print(box)

# 제곱의 결과가 10보다 큰 결과만 담은 list
a = [1, -2, 3, -4, 5]
box = [i for i in a if i * i > 10]
print(box)

box = [i for i in range(10) if i % 3 == 0]
print(box)
