def check(*, key, value):  # 매개변수 받을 때  패킹으로 받거나 아니면 직접 key value값을 넣으라고 명시함
    def set_target():
        for bank in Bank.banks:  # 반복문으로 Bank클래스에 static으로 선언된 banks 리스트를 bank로 각각 돌면서
            for user in bank:  # 위에서 받은 bank를 user가 있는지 반복하는데
                if user.__getitem__(key) == value:  # 만약에 user에 받은 key의 value값이 받아온 value 값이랑 같다면
                    return user  # 해당 user를 리턴해주고
        return None  # 없다면 None 리턴한다

    return set_target  # 그러면 여기엔 검사를 마친 user 혹은 None 값을 리턴해준다


class Bank:  # Bank클래스 선언
    total_count = 3  # total_count static필드 선언
    banks = [[] for i in range(total_count)]  # bank[][]로 선언하는데 컴프리헨션으로 range(토탈 카운트만큼) 리스트를 만들고 그걸 담은 리스트이다

    def __init__(self, owner: str, account_number: str, phone: str, password: str, money: int):  # 생성자 초기화
        self.owner = owner  # 매개변수로 예금주 받아서 클래스 변수 선언
        self.account_number = account_number  # 매개변수로 계좌번호 받아서 클래스 변수 선언
        self.phone = phone  # 매개변수로 전화번호 받아서 클래스 변수 선언
        self.password = password  # 매개변수로 비밀번호 받아서 클래스 변수 선언
        self.money = money  # 매개변수로 돈 받아서 클래스 변수 선언
        self.object = self  # 매개변수로 자기자신 클래스 받아서 클래스 변수 선언

    @classmethod
    def open_account(cls, owner: str, account_number: str, phone: str, password: str, money: int, bank_choice: int):
        # 선언
        bank = [  # 만약에 bank_choice를 1로했을때
            ShinHan,  # ex) [[신한 {"예금주": "임수현", "계좌": 1234, ...} ]] 이값을 bank에 담고 리턴해줬다
            KookMin,
            KaKao
        ][bank_choice - 1]

        # 사용 (bank(owner, ...))
        # 만약에 bank_choice를 1로했을때
        # Back 클래스에 static 으로 선언된 banks 리스트 안에 신한은행 리스트에다가 dict 값을 append 했다
        cls.banks[bank_choice - 1].append(bank(owner, account_number, phone, password, money).__dict__)
        return bank

    @staticmethod
    def check_account_number(account_number: str) -> dict:  # 함수 사용시 매개변수는 str타입으로 받고 함수의 리턴값은 dict로 받으라고 명시!
        return check(key='account_number', value=account_number)()  # check함수에 직접 키 와 벨류에 값을 넣고 이함수 안에있는 함수 값을 리턴했다

    @staticmethod
    def check_phone(phone: str) -> dict:  # 함수 사용시 매개변수는 str타입으로 받고 함수의 리턴값은 dict로 받으라고 명시!
        return check(key='phone', value=phone)()  # check함수에 직접 키 와 벨류에 값을 넣고 이함수 안에있는 함수 값을 리턴했다

    def deposit(self, money: int):  # 입금 함수 받는 매개변수 값은 int로 명시
        self.money += money  # 멤버필드money에 받은 money 값을 더해서 대입하기

    def withdraw(self, money: int):  # 출금 함수 받는 매개변수 값은 int로 명시
        self.money -= money  # 멤버필드money에 받은 money 값을 빼서 대입하기

    def show_balance(self) -> int:  # 잔액 조회 함수 받는 매개변수 값은 int로 명시
        return self.money  # 현재 잔액을 리턴해줌

    def __str__(self):  # 객체 출력시 예쁘게 맴버 필드 출력
        return f'{self.owner}, {self.account_number}, {self.phone}, {self.password}, {self.money}'


class ShinHan(Bank):  # 신한은행
    def deposit(self, money: int):  # 입금함수 오버라이딩
        money /= 2
        super().deposit(money)  # 부모의 입금함수에 /2 값을 넣었다


class KookMin(Bank):
    def withdraw(self, money: int):  # 출금함수 오버라이딩
        money *= 1.5
        super().withdraw(int(money))  # 부모 출금함수에 1.5배의 값을 넣었다


class KaKao(Bank):
    def show_balance(self) -> int:  # 조회함수 오버라이딩
        self.money /= 20
        return super().show_balance()  # 부모 잔액 조회함수에 /20의 값을 넣었다


if __name__ == '__main__':

    bank_menu = "1. 신한 은행\n" \
                "2. 카카오 뱅크\n" \
                "3. 국민 은행\n" \
                "4. 나가기\n"

    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 은행 선택 메뉴로 돌아가기\n"

    owner_message = "예금주: "
    account_number_message = "계좌번호: "
    phone_message = "핸드폰 번호: "
    password_message = "비밀번호(4자리): "
    money_message = "예치금: "
    deposit_message = "입금액: "
    withdraw_message = "출금액: "
    error_message = "다시 시도해주세요"

    while True:
        bank_choice = int(input(bank_menu))  # 은행 선택
        if bank_choice == 4:  # 4번 입력시 프로그램 종료
            break

        while True:
            menu_choice = int(input(menu))  # 은행 선택후 메뉴선택
            if menu_choice == 5:  # 5번 입력시 프로그램 종료
                break

            # 개설
            if menu_choice == 1:
                owner = input(owner_message)  # 예금주 입력받기

                while True:  # 계좌번호 중복검사!
                    account_number = input(account_number_message)  # 계좌번호 입력받기
                    if Bank.check_account_number(account_number) is None:  # 만약에 계좌 중복 검사시 받은 계좌번호가 있다면 계속 다시 입력받게 하기
                        break  # 아니면 중복된게 없다면 받은계좌를 account_number 담기!

                while True:
                    phone = input(phone_message)  # 위 주석과 동일하게 전화번호가 중복되면 다시 입력받고 아니면 받은 전화번호를 phone 담기!
                    if Bank.check_phone(phone) is None:
                        break

                while True:
                    password = input(password_message)  # 비밀번호를 입력받고 받은 길이가 4라면 비밀번호를 담고 아니면 계속 다시 입력받게 하기
                    if password.__len__() == 4:
                        break

                money = int(input(money_message))  # 예치금 입력 받기

                user = None

                # 아래의 분기별 은행 분석을 한 줄로 변경!
                # 위에서 각 검사가 끝난 것들을 Bank의 open_account classmethod에다 넣어주고 그값은 어떤 은행이고 그은행의 유저를 user에 담는다
                user = Bank.open_account(owner, account_number, phone, password, money, bank_choice)

            # 입금
            elif menu_choice == 2:  # 메뉴 2번 일때
                # 입금은 개설한 은행에서만 가능

                # 계좌개설(신한) 입금할 계좌(신한) -> 가능!
                account_number = input(account_number_message)  # 계좌번호 입력후 받기
                user = Bank.check_account_number(account_number)  # 해당계좌가 있는지 검사후 그 user검사한 은행의 계좌명,계좌번호... 등등의 dict을 담고
                if user is not None:  # user가 없을때 ture니깐 true면  현재 user에는 은행의 계좌명,계좌번호... 등등의 dict을 담고있으니 조건식 오케이!
                    if user.__getitem__("password") == input(
                            password_message):  # user의 dict에 키가 password 이고 그 값이 받은 비밀번호면 트루!
                        deposit_money = int(input(deposit_message))  # 입금 할 금액을 받고
                        # 객체를 가져와서 deposite()실행
                        user.__getitem__("object").deposit(deposit_money)  # 해당 user 은행의 객체를 가져와 객체의 메서드 실행했다
                else:  # 아니면 에러메세지
                    print(error_message)
            # 출금
            elif menu_choice == 3:  # 메뉴 3번 선택
                account_number = input(account_number_message)  # 출금할 계좌번호 받기
                user = Bank.check_account_number(account_number)  # 해당계좌가 있는지 검사후 그 user검사한 은행의 계좌명,계좌번호... 등등의 dict을 담고
                if user is not None:  # user가 값이 있다면 참!
                    if user.__getitem__("password") == input(
                            password_message):  # 해당 user 가 즉 어떠한 은행이 가지고있는 "password"키의 값이 입력 받은 값이랑 같다면
                        withdraw_money = int(input(withdraw_message))  # 출금할 금액을 입력 받고 withdraw_money에 담기
                        if user.__getitem__(
                                "object").money >= withdraw_money:  # user가 즉 해당 은행의 객체에 money가 출금할 금액보다 크거나 같다면
                            user.__getitem__("object").withdraw(withdraw_money)  # 해당 은행의 객체의 withdraw() 메서드를 호출한다
                        else:  # 가지고 있는 돈보다 많은 금액을 출금할때
                            print("대출을 진행할까요?")
                else:  # user가 None일때
                    print(error_message)
            # 잔액
            elif menu_choice == 4:  # 메뉴 4 입력시
                account_number = input(account_number_message)  # 잔액조회할 계좌 받기
                user = Bank.check_account_number(account_number)  # 해당계좌가 있는지 검사후 그 user검사한 은행의 계좌명,계좌번호... 등등의 dict을 담고
                if user is not None:  # user가 값이 있다면 참!
                    if user.__getitem__("password") == input(
                            password_message):  # 해당 user의 키값이 "password"의 값이 입력받은 값과 동일하면
                        print(
                            f'현재 잔액: {user.__getitem__("object").show_balance()}')  # 해당 user의 객체의 show_balance() 호출후 출력

                else:  # user가 None일때
                    print(error_message)
