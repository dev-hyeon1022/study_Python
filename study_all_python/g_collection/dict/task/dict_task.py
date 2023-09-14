# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새올운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
admin_dict = {}

name_list = []
price_list = []

title = ""
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"

message_add = "상품명과 가격을 입력해주세요\n:"
message_ist = "상품명을 입력해주세요\n:"
message_ist_add = "상품명과 가격을 입력해주세요\n:"
message_remove = "삭제할 상품명을 입력해주세요\n:"
message_search = "1.상품명 검색\n2.가격 검색\n:"

while True:
    choice = int(input(title + "\n" + menu))

    # 추가
    if choice == 1:
        name_add, price_add = input(message_add).split(" ")
        if name_add not in admin_dict:
            admin_dict[name_add] = int(price_add)
        else:
            print("이미 있는 상품입니다")

    # 수정
    elif choice == 2:
        name_ist = input(message_ist)
        if name_ist in admin_dict:
            name_new, price_new = input(message_ist_add).split(" ")
            del admin_dict[name_ist]
            admin_dict[name_new] = int(price_new)
        else:
            print("존재하지 않는 상품입니다")

    # 삭제
    elif choice == 3:
        name_remove = input(message_remove)
        if name_remove in admin_dict:
            del admin_dict[name_remove]
        else:
            print("존재하지 않는 상품 입니다")

    # 검색
    elif choice == 4:
        num = int(input(message_search))
        if num == 1:
            name_ser = input("검색할 상품명을 입력하세요\n")
            if name_ser in admin_dict:
                for key, value in admin_dict.items():
                    print(f"{key} - {value}")
                    break
            else:
                print("검색하신 상품이 없습니다.")

        elif num == 2:
            check = False
            price_ser = int(input("검색할 가격을 입력하세요:\n"))
            min = price_ser * 0.5
            max = price_ser * 1.5

            for key, value in admin_dict.items():
                if min <= value <= max:
                    check = True
                    print(f'{key} - {value}')

            if not check:
                print("검색하신 가격대가 없습니다")

        else:
            print("ex)1 or 2")

    # 목록
    elif choice == 5:
        if len(admin_dict) == 0:
            print("등록된 정보가 없습니다")
            continue
        for i, j in admin_dict.items():
            print(f"{i} - {j}")

    # 나가기
    elif choice == 6:
        break

    # 그 외
    else:
        print("1~6 사이의 숫자를 입력해주세요")