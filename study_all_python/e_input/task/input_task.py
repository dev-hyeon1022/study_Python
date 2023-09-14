# email을 입력받고 아이디(email_id)와 도메인(domain)을 각각 변수에 담고 출력
email_id, domain = input("이메일을 입력하시오: ").split("@")
frommatting = f"{email_id}\n{domain}"
print(frommatting)

'''
첫 번째 값으로 야드를 입력받고, 두 번째 값으로 인치를 입력받아서
각각 cm로 변환하여 다음 형식에 맞추어 소수점 둘 째자리까지 출력한다.

1yd: 91.44cm
1in: 2.54cm

예)
    yard 입력: 10
    inch 입력: 10

    10 yard는 914.4cm
    10 inch는 25.4cm
'''

yard = float(input("yard 입력: "))
inch = float(input("inch 입력: "))
frommatting = f"{int(yard)} yard는 {yard * 91.44}cm\n{int(inch)} inch는 {inch * 2.54}cm"
print(frommatting)
