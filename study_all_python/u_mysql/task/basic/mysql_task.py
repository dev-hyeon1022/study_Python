from u_mysql.crud import save, find_all, find_one_id, update, delete

# 아이디 중복검사
# 회원가입(SMS API) - 랜덤한 인증번호 6자리 발송 후 검사
# 회원 비밀번호 변경(EMAIL API) - 랜덤한 인증번호 10자리 발송 후 검사

# 사용자가 입력한 문장을 영어로 번역
# 한국어와 번역된 문장을 DBMS에 저장
# 번역 내역 조회

# 업로드한 이미지 파일의 이름과 이미지의 내용을 DBMS에 저장(OCR API)




def sign_on(name: str, email_id: str, password: str, phone: str):
    select_query = 'select user_email_id from tbl_user'

    insert_query = 'insert into tbl_user(user_name, user_email_id, user_password, user_phone)' \
                   'values(%s, %s, %s, %s)'
    insert_param = [name, email_id, password, phone]

    #아이디 중복 검사
    for i in find_all(select_query):
        if i.get("user_email_id") == email_id:
            return print("중복된 아이디입니다")

    save(insert_query,insert_param) #테스트를 위한 함수 사용 나중엔 인증번호 검사후 사용예정
    print("아이디 사용가능")



sign_on("홍길동", "hgd1234@gmail.com", "1234", "01012345678")





