# '택시'에서 승객들에게 공통적으로 적용되는 자료
# - 기본 요금 : 5800원
# - 기본 주행 거리 : 2km
# - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원

# 택시 객체 생성시 승객별로 돈과, 거리를 받아서 생성

# 거리에 따른 요금 계산 메소드 정의
# 거리에 따른 잔돈 계산 메소드 정의

class Taxi:
    basic_price = 5800
    basic_km = 2

    def __init__(self, price_peple, km):
        self.price_peple = price_peple
        self.km = km

    def km_price(self):
        print(f"요금:{Taxi.basic_price + (self.km - Taxi.basic_km) * 1000}입니다")

    def 잔돈(self):
        all_price = Taxi.basic_price + (self.km - Taxi.basic_km) * 1000
        잔돈 = self.price_peple - (Taxi.basic_price + (self.km - Taxi.basic_km) * 1000)
        print(f"받은돈:{self.price_peple} - 요금:{all_price} = 잔돈:{잔돈}입니다")


peple = Taxi(10000, 3)
peple_4 = Taxi(20000, 4)

peple.km_price()
peple.잔돈()

peple_4.km_price()
peple_4.잔돈()


# ==========================================================================
# 혜빈님 소스코드
class Taxi:
    def __init__(self, passenger, fee=5800, distance=0):
        self.passenger = passenger
        self.fee = fee
        self.distance = distance

    def calculate_fee(self):
        total = 0
        if self.distance > 2:
            total = (self.distance - 2) * 1000 + 5800
        else:
            total = self.fee

        return total

    def calculate_change(self):
        change = 0
        if self.distance > 2:
            change = self.fee - ((self.distance - 2) * 1000)
        else:
            change = self.fee - 5800
        return change


pass1 = Taxi("승객 1", 50000, 24)
pass2 = Taxi("승객 2", 30000, 14)
pass3 = Taxi("승객 3", 80000, 31)

print(pass1.calculate_fee())
print(pass2.calculate_fee())
print(pass1.calculate_change())
print(pass3.calculate_change())

# ===============================================================================================
# 강사님 소스코드

# '택시'에서 승객들에게 공통적으로 적용되는 자료
# - 기본 요금 : 5800원
# - 기본 주행 거리 : 2km
# - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원

# 택시 객체 생성시 승객별로 돈과, 거리를 받아서 생성

# 거리에 따른 요금 계산 메소드 정의
# 거리에 따른 잔돈 계산 메소드 정의
class Taxi:
    init_fare = 5800
    init_distance = 2
    fare_per_km = 1000

    def __init__(self, money, distance):
        self.money = money
        self.distance = distance

    def calc_cost(self):
        cost = Taxi.init_fare
        if self.distance > Taxi.init_distance:
            cost += (self.distance - Taxi.init_distance) * Taxi.fare_per_km

        return cost

    def get_change(self):
        change = self.money - self.calc_cost()
        return change


passenger1 = Taxi(20000, 1)
passenger2 = Taxi(30000, 10)

print(passenger1.calc_cost(), passenger1.get_change())
print(passenger2.calc_cost(), passenger2.get_change())


# PartTimer

# '모든 직원'에 공통적으로 적용되는 내용
# - 시급
# - 직원수

# '각 직원'별로 적용되는 내용
# - 별명
# - 근무지(기본값: '청담동')
# - 급여 총액(초기값: 0, 생성자로 초기화 불가능)

# 직원 급여 계산
#   '근무 시간 + 상여금'에 따른 직원 급여 계산
#   '상여금'은 지정 하지 않으면 0 으로 처리


class PartTimer:
    time_money = 10000
    total_peple = 0

    def __init__(self, name, workplace = "청담동", total_price = 0):
        self.name = name
        self.workplace = workplace
        self.total_price = total_price
        PartTimer.total_peple += 1
        print(f"총 직원 수:{PartTimer.total_peple}")
    def partTimer_price(self, worktime, bonus = 0):
        self.total_price = PartTimer.time_money * worktime + bonus

        print(f"{self.name}님 근무지:{self.workplace}\n"
              f"시급:{PartTimer.time_money}원 근무시간:{self.worktime}"
              f"시간 상여금:{self.bonus}원 총 급여:{self.total_price}원")



man = PartTimer("임수현","역삼역")
man.partTimer_price(22,50000)


man1 = PartTimer("임수현","역삼역")

man2 = PartTimer("임수현","역삼역")







