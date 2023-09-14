import os
import psutil

process_object = psutil.Process(os.getpid())

############################################################################
memory_before = process_object.memory_info().rss / 1024 / 1024

data_list = [i ** 2 for i in range(100)]
# TypeError: 'list' object is not an iterator
# print(next(data_list))
print(data_list)

memory_after = process_object.memory_info().rss / 1024 / 1024
print(f'memory: {memory_before} -> {memory_after}')

############################################################################

# data_iterator = iter(data_list)
# print(type(data_iterator))
# print(next(data_iterator))

############################################################################
memory_before = process_object.memory_info().rss / 1024 / 1024

data_generator = (i ** 2 for i in range(100))
# print(type(data_generator))
print(next(data_generator))

memory_after = process_object.memory_info().rss / 1024 / 1024
print(f'memory: {memory_before} -> {memory_after}')


############################################################################

def increase(number: int = 0): #number매개변수에 int값을 받아
    while True:                #무한루프 돌리기
        number += 1            #받은 number값에 1증가
        yield number           #number 값을 함수 밖에서 전달해서 진행중인 함수를 일시정지함
                               # 이때 전달된 값이 next로 사용됬다면 다시 무한루프 진행


result = increase()            #yield로 전달한값을 result에 담고
while True:
    data = input("다음[y/N] >> ")
    if data == 'y':
        print(next(result))   #그 값을 그냥 출력하면 주소값이 나오니 next로 변환해서 출력시 값이 출력된다!
    else:
        break