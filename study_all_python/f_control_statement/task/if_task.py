# 사용자에게 아래의 메뉴를 출력하고 번호를 입력받는다.

# 1. 빨간색
# 2. 검은색
# 3. 노란색
# 4. 흰색

# 사용자가 입력한 번호의 색상을 영어로 출력한다.

message_red = "1. 빨간색"
message_black = "2. 검은색"
message_yellow = "3. 노란색"
message_white = "4. 흰색"
num = int(input(message_red + "\n" + message_black + "\n" + message_yellow + "\n" + message_white + "\n: "))

if num == 1:
    print("red")
elif num == 2:
    print("black")
elif num == 3:
    print("yellow")
elif num == 4:
    print("white")
else: print("1~4중 입력하시오")
