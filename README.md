# **코리아 IT 아카데미 국비과정** 
## Python 😺 
<a name="readme-top"></a>
#### PYTHON - 프로그래밍 언어
    컴퓨터와 소통하기 위해 사용하는 언어이며,
    간결한 문법과 빠른 연산속도 등의 다양한 장점을 가지고 있어서 인기 있는 언어이다.
    GUI 개발, 웹 개발, 데이터 분석, AI 등에 사용한다.
#### 소스코드 
    명령어를 작성해 놓은 것. 
    개발자와 컴퓨터가 소통할 것을 글로 작성해 놓은 것.  
#### 컴파일
    사람의 언어를 컴퓨터 언어로 바꿔주는 작업.
#### 컴파일러
    소스코트 -> 컴파일러 -> 기계어 -> 운영체제 -> 하드웨어
    컴파일을 해주는 프로그램 또는 명령어
    코드 수정 후 실행할 때 전체 컴파일 진행
    일괄 처리이기 떄문에 실행 속도 비교적 빠름
    번역 파일이 생성되며, 실제 소스코드가 유출될 수 없음.
#### 컴파일러 해석 방향
    위에서 아래로 좌에서 우로 번역.
#### 콘솔
    개발자와 운영체제가 소통한 결과를 보여주는 창.
#### 프로그램
    소스코드로 잘 짜여진 틀.
    
#### ▶ 일반프로그램
    프로그램
	OS(운영체제): 하드웨어에 적절한 전기신호를 흘려주는 역할.
	하드웨어

	- 일반 프로그램은 이식성이 좋지 않다.
#### ▶ PYTHON 프로그램
    프로그램
    PVM: PYTHON 프로그램을 OS에 맞게 번역한다.
    OS
    하드웨어
	
	- PYTHON 프로그램은 이식성이 좋다.
   
-------------------------------------------------------------------------------------

#### 출력 함수
	print(): 입력 받은 값을 출력해주며 sep, end, file 매개변수를 통해 원하는 형태로 출력 할 수 있다.
 
#### 출력 함수 목적
	전달받은 데이터 및 전달할 데이터 검사, 오류 발생 지점 구체화 및 검사
  
-------------------------------------------------------------------------------------

#### 변수 : 저장공간
	
     x	      =  10
     저장공간의 대입	  값
     이름	          연산자

#### 자료형(type, 종류)
    동적 바인딩: 값에 따라 자료형이 정해진다

    자료형(type)       값
    정수(int)          0, 10, -187, ...
    실수(float)        0.0, 10.58, -77.568, ...
    문자열(str)        '0', "0.0", """홍길동""", '''Python''', ...
    리스트(list)       [1, 2, 3], [0], [3,], ...
    튜플(tuple)        (1, 2), (), 1, 2, 3, (1,), ...
    딕셔너리(dict)     {key:value,}, ...
    집합(set)          {1, 2, 3}, {1}, ...
    불린(bool)         True, False

#### 변수의 선언
    name = value
    예)
    x = 10
    x라는 이름의 저장공간이 할당(allocation)되고 그 안에 10이 들어간다.

#### 변수의 사용
	data = 20 // 선언
	print(data + 9) // 사용
	data = data + 7 // 선언, 사용
	data - 9 // 사용

#### 변수의 선언
	변수명 = 초기값 //초기화
	변수명

#### 변수의 선언 시 주의사항
	1. 같은 이름의 변수로 선언할 수 없다.
	2. 초기화를 해준다.
	3. 되도록 선언부에 한꺼번에 선언한다(영역 상단).

#### 변수명 주의사항
	문자로 시작해야 한다.
	특수문자는 사용할 수 없다. 단, _는 허용한다.
	소문자로 시작한다.
	공백을 사용할 수 없다.

 	GoodBoy : 파스칼 표기법(클래스명, 오류명),
	goodBoy : 카멜 표기법(JAVA),
	good_boy : 스네이크 표기법(변수, 함수)
 	good-boy : 케밥 표기법(HTML, CSS)

	되도록 한글은 사용하지 않는다.
	명사로 사용한다.
	뜻이 있는 단어를 사용한다.
	a, b, c, d, e, ... (X)
	data, number, age, name, ...(O)

#### 변수를 사용하는 이유
	1. 반복되는 값을 쉽게 관리할 수 있다.
	2. 의미 없는 값을 하나의 정보로 만들기 위해서(자료구조).

-------------------------------------------------------------------------------------

#### 서식문자(format)
    반드시 따옴표 안에서 작성한다

    ----------------------------------
    서식문자   설명
    ----------------------------------
    %d           10진수 정수 표현
    %f           실수 표현
    %s           문자열 표현
    ----------------------------------

-------------------------------------------------------------------------------------

#### 형변환
	- 자동 형변환
		정수 + 정수 = 정수
		정수 + 실수 = 실수
		3 + 0.0 = 3.0
		5 / 2 = 2.0

	- 강제 형변환
		bin(), oct(), hex(), int(), float(),str(),bool()
		
<p align="right">(<a href="#readme-top">back to top</a>)</p>

-------------------------------------------------------------------------------------

#### 입력
	커서가 깜빡이고 있는 상태. 
	항상 입력 전 출력을 통해 사용자가 정확한 값을 입력할 수 있도록 한다.

#### 입력 함수
	쉘 또는 콘솔에서 입력을 받아야 할 때 사용하며, 입력받은 값은 문자열 값으로 리턴된다.
	input("출력할 메세지")

-------------------------------------------------------------------------------------

#### 연산자
	기능이 있는 특수문자.
 
	1.산술 연산자

        ----------------------------------
        연산자   예시   설명
        ----------------------------------
        +       3 + 5   더하기
        -       3 - 5   빼기
        *       3 * 5   곱하기
        /       3 / 5   나누기
        **       3 ** 5   제곱
        //       3 // 5   몫
        %       3 % 5   나머지
        ----------------------------------

	2.대입(allocation) 연산자

        -------------------------------------------
        연산자   예시           설명
        -------------------------------------------
        =       data = 10       좌항에 우항을 대입
        +=       data += 10       data = data + 10
        -=       data -= 10       data = data - 10
        *=       data *= 10       data = data * 10
        /=       data /= 10       data = data / 10
        **=      data **= 10       data = data ** 10
        //=      data //= 10       data = data // 10
        -------------------------------------------

	3.비교 연산자

        ※ 조건식 - 참 또는 거짓, 둘 중 하나가 나오는 식
        ※ 조건식은 항상 값으로 본다(True 또는 False)

        ----------------------------------------------------------------
        연산자   예시                   설명
        ----------------------------------------------------------------
        ==       data == 10               같으면 True, 같지 않으면 False
        !=, <>   data != 10, data <> 10   같지 않으면 True, 같으면 False
        >       3 > 5                   보다 크다
        <       3 < 5                   보다 작다
        >=       3 >= 5                   이상
        <=       3 <= 5                   이하
        ----------------------------------------------------------------

	4.논리 연산자

        ----------------------------------------------------------------
        연산자   예시               설명
        ----------------------------------------------------------------
        and       a == b and c == d   조건식 둘 다 True일 경우 True
        or       a == b or c == d   조건식 둘 중 하나라도 True일 경우 True
        not       not (a == b)       True를 False로 False를 True로 변경
        ----------------------------------------------------------------

	5.멤버 연산자

        -----------------------------------------------------------------------------------------------------
        연산자   예시                                   설명
        -----------------------------------------------------------------------------------------------------
        in       "a" in "abc", 2 in [1, 2, 3]           좌항이 우항에 포함되었다면 True 아니면 False
        not in   "a" not in "abc", 2 not in [1, 2, 3]   좌항이 우항에 포함되어 있지 않다면 True 포함되면 False
        -----------------------------------------------------------------------------------------------------

	6.식별 연산자

        -----------------------------------------------------------------------------------------------------
        연산자   예시                                       설명
        -----------------------------------------------------------------------------------------------------
        is       a = 10; b = a; a is b                       두 객체 모두 같은 주소일 경우 True 아니면 False
        is not   a = [1, 2, 3]; b = [1, 2, 3]; a is not b   두 객체 모두 같은 주소일 경우 True 아니면 False
        -----------------------------------------------------------------------------------------------------

<p align="right">(<a href="#readme-top">back to top</a>)</p>

----------------------------------------------------------------------------------

#### 조건문
	if문: 주어진 조건이 참(True)이면 특정 코드를 실행하고, 거짓(False)이면 실행하지 않는 파이썬 제어 구조.
	if 조건식:
		실행할 문장
	
	if 조건식:
		실행할 문장

 	if 조건식:
		실행할 문장
	....


	if 조건식:
		실행할 문장
	
	else if: 조건식
		실행할 문장
	
	else: 
		실행할 문장
  
-------------------------------------------------------------------------------------------------
#### 반복문
	for문: in절 뒤의 요소를 순서대로 변수에 담고 다음 값이 더 이상 없을 경우 종료.
 
	1.for문	
		for 변수명 in range(inclusive_start, exclusive_end, step):
            	실행할 문장
	     
	2.while문
		while 조건식:
            	실행할 문장


for문과 while문의 목적
	- for : 몇 번 반복할 지 알 때
	- while : 몇 번 반복할 지 모를 때

---------------------------------------------------------------------------------------------

#### 기타 제어문
	break : 즉시 해당 중괄호 영역을 탈출한다.
		- if문 안에서 사용 시 if문을 탈출하지 않고 해당 if문이 포함된 영역을 탈출한다.

	continue : 즉시 다음 반복.
		- 아래의 코드를 실행하지 않기 위해서 사용한다.
    
<p align="right">(<a href="#readme-top">back to top</a>)</p>
    
---------------------------------------------------------------------------------------------

### 컬렉션
    많은 데이터를 쉽고 효과적으로 관리할 수 있는 표준화된 방법을 제공하는 클래스들의 집합.

#### list : 저장공간의 나열

    사용 목적
    	1.여러 번 선언하지 않고 한 번만 선언하기 위해서 사용
       	   변수를 여러 번 선언하면 관리하기 힘들기 때문에 여러 칸 list로 한 번 선언

    	2.규칙성 없는 값에 규칙성을 부여하기 위해서 사용

#### list 선언
	list명 = [값1, 값2, ...]
    	list명 = [값] * 칸수
    	list명 = list(range(start, end, step))

#### list 구조
	data_list = [3, 5, 1, 2, 8]

	data_list라는 이름의 저장공간은 한 개 만들어지며, 여기에는 한 개의 값만 담을 수 있다.
	5개의 값을 담기 위해서는 5칸이 필요하며, 이는 Heap 메모리에 할당된다. 5칸의 저장공간 중
	첫 번째 저장공간의 주소값이 data_list 저장공간으로 들어가며, 다음 주소에 접근하기 위해서는
	+ n을 한다. 예를 들어 data_list + 2는 1이라는 값이 담긴 주소값이 되고,
	PYTHON에서는 직접 주소에 접근하는 연산자가 없기 때문에 위와 같은 식을 []로 치환하여 사용하며, 
 	data_list[2]로 사용한다. 각각의 방 번호는 index라고 부르며, 
  	배열은 시작주소를 가지고 있기 때문에 인덱스 번호는 항상 0부터 시작된다.

#### list 길이
 	data_list = [3, 5, 1, 2, 8]
  
 	len 함수를 사용하여 list의 길이를 반환해준다
  	len(data_list) // 5

#### list 사용
	data_list = [1, 2, 3]
 
    	- 값 넣기
           (추가)
               list명.append(값)
               data_list.append(4)
               결과: [1, 2, 3, 4]

           (삽입)
               list명.insert(인덱스번호, 값)
               data_list.insert(1, 1.5)
               결과: [1, 1.5, 2, 3, 4]

    	- 값 삭제
           list명.remove(값)
               중복 시 먼저 나온 값(낮은 인덱스 값)이 삭제

           del(list명[인덱스])
           del list명[인덱스]
               인덱스로 삭제

           list명.clear()
               모든 값 삭제

    	- 값 검색
           list명.index(값)
           값이 들어 있는 저장공간의 인덱스 번호
           중복 시 먼저 나온 값의 인덱스 번호

    	- 값 수정
           list명[인덱스] = 새로운 값


#### dict: 키와 값으로 매칭된 데이터 타입
	한 쌍으로 저장되어 관리되어 저장된다.
 	len()를 사용하면 한 쌍을 1로 카운트한다.
  	키 값은 중복이 될 수 없지만 값은 중복이 가능하다.
   	키 값을 주면 그 키의 값을 가지고 온다.

#### dict 선언
    dict명 = {키: 값, 키: 값, ...}

#### dict 사용
	- 추가, 수정
           dict명[키] = 값
           dict명.update({k:v, k:v, ...}), 있으면 수정, 없으면 추가

	- 삭제
           del dict명[키]

	- 검사
           키 in dict명: 키가 있으면 참
           키 not in dict명: 키가 없으면 참


#### set: 집합 자료형
 	저장 순서가 없다.
	고유한 값을 가집니다. (값 중복 불가능)
 	set 키워드를 사용하거나 중괄호를 이용해서 표현가능
	
#### set 선언
	set명 = set([1, 2, 3])
	set명 = set({1, 2, 3})
	set명 = {1, 2, 3}
	
#### set 사용
	- 중복 삭제
 	   set명 = set([1,1,2,3,4,5])


#### tuple: 값이 변하지 않는 데이터 타입
	값이 중복될 수 있다.
 	tuple의 요소 값은 변경하거나 삭제할 수 없다.

#### tuple 선언
	tuple명 = (1, 2, 3, 4, 5)
 	tuple명 = (1,)
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

--------------------------------------------------------------------------------

#### 함수
	이름 뒤에 소괄호, 작성된 코드의 주소값을 담고 있는 저장공간.

##### 함수 선언
	def 함수명(매개변수, ...):
        실행할 문장
        return 리턴값

##### 함수 목적
	1. 재사용(특정성을 부여해서는 안된다).
	2. 소스코드 간결화

---------------------------------------------------------------------

#### 클로저(closure, 폐쇄): 함수 안에 함수, 모듈화
	함수가 정의된 시점의 변수를 기억하고, 이 변수를 나중에 참조 혹은 변경이 가능하도록 해주는 문법이다.
 	내부 영역에 선언된 변수는 외부에서 접근이 불가능하기 때문에 데이터 은닉을 할 수 있으며,
     	함수가 종료된 이후에도 지역변수에 접근할 수 있기 때문에 데이터 지속성을 가지고 있다.
     	또한 다른 함수를 인자로 받거나 리턴할 수 있는 함수형 프로그래밍이 가능해진다.
     	하지만 코드 복잡성이 증가하고 지역변수를 메모리에 유지하기 때문에 메모리 사용량이 증가될 수 있다.
     	
      	사용 예시)
	  def out(arg):
    	      def in(arg):
        	  value = operate something
        	  return value
    	  return in
       
        하지만 파이썬에서는 클래스를 지원하기 때문에 클로저를 굳이 구현할 필요성은 없다.
        클래스 내부에 함수를 선언하고 객체를 만들어서 사용할 수 있기 때문에,
        클래스를 지원하지 않는 언어에서 클래스 방식으로 설계하기 위해 클로저를 사용한다.
        Javascript언어가 클로저 방식을 사용하는 대표적인 언어이다.

---------------------------------------------------------------------


#### 클래스(반)
	공통요소를 한 번만 선언해놓고 가져다 사용만 하도록 설계한다.

	1. 타입이다.
		클래스 안에 선언된 변수와 메소드를 사용하고 싶다면,
		해당 클래스 타입으로 객체를 선언해야 한다.

	2. 주어이다.
		원숭이가 먹는다 바나나를.
		Monkey.eat("바나나");

#### 클래스 선언
	class 클래스명:
            필드(변수, 메소드)

#### 클래스의 필드 사용
	1. 객체화(instance): 객체(instance variable)를 만드는 작업, 추상적인 개념을 구체화시키는 작업
           객체명 = 생성자()
           객체명.필드명
           ※ .(마침표): 하위 연산자, 멤버변수 접근 연산자, 닷 연산자, 점 연산자
                         주소값 뒤에서만 사용이 가능하며 해당 주소를 참조(접근)하는 명령어이다.
			 
	2. static: 모든 객체가 공유하는 필드이며, 무조건 객체가 아닌 클래스로 직접 접근할 수 있다.
           ※ 만약 static필드를 객체로 접근하면 그 필드는 그 객체에 새롭게 선언된다.
           즉, static 필드는 무조건 클래스 이름으로 접근해야 한다.
           만약 객체로 static 필드를 접근하여 read형태로 사용할 수 있으나,
           write형태로 사용하면 self에 선언된다.
        class A:
            static_variable = 0

        print(A.static_variable)

#### 생성자
	클래스 이름 뒤에 소괄호가 있는 형태, 메소드와 기능이 똑같지만 메소드라고 부르지 않는다.
    	생성자는 리턴이라는 기능이 존재하지 않기 때문이다.

#### 기본 생성자
	매개변수가 없는 생성자이며, 클래스 선언 시 자동으로 선언된다.
    	사용자가 직접 생성자를 선언하게 되면 자동으로 선언되지 않는다.

#### self
	필드에 접근한 객체가 누구인지 알아야 해당 필드에 접근할 수 있다.
   	이 때 접근한 객체가 가지고 있는 필드의 주소값이 self라는 변수에 자동으로 담긴다.
	
<p align="right">(<a href="#readme-top">back to top</a>)</p>
  
----------------------------------------------------------------------------------------------

#### Storage class(저장 기억 부류)

		Stack		Data영역
		지역변수, 매개변수	전역변수, 정적변수(static)

1. 초기화		직접		자동	
2. 생명주기	}		new, 프로그램 종료 시

static
	모든 객체가 공유해야 할 때 사용한다.
  
--------------------------------------------------------------------------------------------

#### 다형성(polymorphism)
	1. 오버로딩(Overloading)
		매개변수의 개수 또는 타입이 다르면 동일한 이름의 메소드로 선언할 수 있다.
	2.
  
-----------------------------------------------------------------------------------------------

#### 클래스 심화 실습
	- 주제: 원하는 직업을 클래스로 선언
	- 반드시 수익 창출이 되어야 한다.
	- 확률을 추가한다.
	- 구현에 필요한 필드는 얼마든지 추가 선언이 가능하다.
		예) 승진, 티어 승급, 연속 5회 성공 시 레벨 업 등


---------------------------------------------------------------------------------------------
#### 상속(inheritance)
	1. 기존에 선언된 클래스의 필드를 새롭게 만들 클래스의 필드로 사용하고자 할 때
	2. 여러 클래스 선언 시 필드가 겹칠 때 부모 클래스를 먼저 선언하고 공통 필드를 묶어서
	   자식 클래스들에게 상속해준다.

#### 상속 문법
	class A {
		A 필드
	}

	class B extends A{
		A, B 필드
	}

A: 부모 클래스, 상위 클래스, 슈퍼 클래스, 기반 클래스
B: 자식 클래스, 하위 클래스, 서브 클래스, 파생 클래스

##### super() : 부모 생성자
	자식 클래스 타입의 객체로 부모필드에 접근할 수 있다.
	하지만 자식 생성자만 호출하기 때문에, 자식 필드만 메모리에 할당된다고 생각할 수 있다.
	사실 자식 생성자에는 항상 부모 생성자를 호출하기 때문에 자식 생성자 호출 시 부모와 자식 필드 모두
	메모리에 할당된다. 이 때 부모 생성자를 호출하는 방법은 super()를 사용하는 것이다.
	만약, super()를 작성하지 않더라도 컴파일러가 자동으로 작성해준다.

##### 다형성(polymorphism)
	1. 오버로딩
	2. 오버라이딩(재정의)
		부모 필드에서 선언한 메소드를 자식 필드에서 수정하고자 할 때 재정의를 해야 한다.
		이는 자식에서 부모 필드의 메소드와 동일한 이름으로 선언하는 것이다.
		부모 필드가 메모리에 먼저 할당되고 a라는 메소드가 먼저 올라간다고 하면,
		자식 필드가 메모리에 할당되면서 재정의한 a메소드가 새롭게 만들어지는 것이 아니라
		기존에 할당된 a메소드 저장공간에 새롭게 재정의한 자식 필드의 소스코드 주소가 들어가게 된다.
		따라서 자식 객체로 a메소드에 접근하면 자식 필드에서 재정의한 소스코드의 내용이 읽히게 된다.
		
-------------------------------------------------------------------------------------------------
#### 접근 권한 제어자(접근자)
	default: 다른 패키지에서 접근 불가
	public: 모든 곳에서 접근 가능, 해당 파일의 메인 클래스일 경우만 사용 가능
	protected: 다른 패키지에서 접근 불가, 자식은 가능
	private: 다른 클래스에서 접근 불가, 메소드(getter, setter)로만 접근하자!

-------------------------------------------------------------------------------------------------
※ 모든 자식은 부모타입이다.

#### Casting
	1. up casting : 자식 값을 부모타입으로 형변환
	2. down casting : up casting된 객체를 자식타입으로 형변환
	※ 부모 값을 자식 타입으로 형변환 시 오류

#### Casting을 사용하는 이유
	모든 자식 값을 전달받기 위해서는 동일한 타입의 저장공간으로 받아야 한다.
	하지만 자식끼리는 서로 타입이 다르기 때문에 한 번에 전달받을 수가 없다.
	이 때 up casting을 사용하면, 모든 자식이 부모 타입이므로 하나의 저장공간에
	모든 자식을 받을 수 있게 된다.
	만약 up casting으로 자식 값을 전달받았다면, 자식에서 새롭게 구현한 기능들은 사용할 수 없기 때문에
	down casting을 통해서 복구하여 사용한다.

<img width="1000" src="https://github.com/code-hyun/study-java/assets/122762287/6ef2552a-c408-4600-b830-2b5d6f86a6f8">

#### instanceof(객체 간 타입 비교)
	a instanceof A : 조건식

	- a가 A타입이면 true
	- a가 A타입이 아니라면 false

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---------------------------------------------------------------------

#### 추상 클래스
	필드 안에 구현이 안된 메소드가 선언되어 있는 클래스를 추상 클래스라고 한다.
	이 때 구현되지 않은 메소드를 추상 메소드라고 부른다.
	반드시 재정의를 통해 구현을 해야지만 메모리에 할당되기 때문에
	"강제성"을 부여하기 위해서 추상 메소드로 선언한다.

#### 추상 클래스 선언
	abstract class 클래스명 {
		abstract 리턴타입 메소드명(매개변수, ...);
		일반 메소드 선언가능.
	}
  
---------------------------------------------------------------------

#### 인터페이스(interface) : 틀
	추상 클래스를 고도화시킨 문법.
	상수와 추상메소드만 존재한다.
	구현은 지정한 클래스에서 진행하고, 인터페이스를
	다른 클래스에 지정할 때에는 implements 키워드를 사용한다.
	
#### 추상 클래스와 인터페이스 간의 관계
	인터페이스를 클래스에 바로 지정하면 모든 메소드에 강제성이 부여되어서
	전부 다 구현해야 한다. 하지만 일반적인 상황에서는 모든 것이 아닌,
	필요한 메소드를 골라서 재정의해야한다.
	인터페이스를 직접 지정하지 않고 다른 클래스에 지정한 후 바디를 만들어 놓는다면,
	강제성이 소멸되고 이 클래스를 상속받아서 필드를 구현한다면, 골라서 재정의할 수 있게 된다.
	이 때 중간에서 강제성을 없애주는 클래스를 추상클래스로 선언하기로 하며,
	추상클래스 이름 뒤에는 Adapter를 붙여서 목적을 알려준다.
  
--------------------------------------------------------------------------------------

#### 마커 인터페이스(Marker Interface)
	클래스들을 그룹화하기 위한 목적으로 사용한다.
	인터페이스는 지정한 클래스의 부모이며, 모든 자식은 부모의 타입이므로
	마커 인터페이스를 지정받은 클래스들이 하나의 타입으로 묶이게 된다.
	이름 뒤에 Marker를 붙여줘야 한다.
  
--------------------------------------------------------------------------------------

#### 내부 클래스(Inner Class)
	하나의 클래스에서 a작업과 b작업이 있을 때에는 따로 분리하여 클래스로 만들지 않고,
	클래스 안에 클래스를 선언하여 설계한다. 이 때 밖에 있는 클래스를 외부 클래스라고 하며,
	안에 선언된 클래스를 내부 클래스라고 한다. 외부 클래스가 메모리에 할당되어야
	내부 클래스를 객체화할 수 있기 때문에 클래스를 숨기기 위해서 내부 클래스를 사용하기도 하며,
	이를 캡슐화 또는 은닉화라고 한다. 내부 클래스는 외부 클래스의 필드이기 때문에
	외부 클래스의 필드를 자신의 필드처럼 가져다 사용할 수 있지만 상속관계가 아니기 때문에
	내부 클래스일지라도 extends를 통해 다른 클래스를 상속받아서 사용할 수 있다.

#### 익명 클래스(Anonymous Inner Class)
	이름이 없는 클래스이며 구현되지 않은 필드를 구현하기 위해 일회성으로 생성되는 클래스이다.
  
----------------------------------------------------------------------------------------

#### 다중 상속
	여러 부모 클래스를 상속하는 것을 다중 상속이라고 한다.
	JAVA는 모호성 때문에 다중 상속을 지원하지 않는다.
	하지만 JDK8버전부터는 인터페이스에 default메소드를 선언할 수 있으며,
	여러 개를 지정할 수 있는 인터페이스 특성상 다중 상속을 지원하는 것이나 다름이 없다.

#### 모호성(ambiguity)
	하나의 자식이 여러 부모를 상속받을 때 부모 필드에 동일한 이름의 필드가 있다면,
	어떤 부모의 필드인지 알 수가 없다. 이를 모호성이라고 부른다.

#### 모호성 해결 방법
- 상황1: 두 개의 인터페이스 내에 이름과 매개변수가 똑같은 메소드가 선언되어 있다.
- 해결1: 자식 클래스에서 재정의하여 사용한다. 
        원하는 부모의 필드에 접근하기 위해서는 재정의된 메소드에서 "부모명.super.필드명"을 작성한다.

- 상황2: 부모 클래스의 메소드와 인터페이스의 디폴트 메소드의 이름과 매개변수가 똑같이 선언되어 있다.
- 해결2: 부모 클래스의 메소드가 사용된다.

----------------------------------------------------------------------------------------

#### 함수형 인터페이스(Functional interface)
	인터페이스 중 추상 메소드를 하나만 가지고 있는 인터페이스를 함수형 인터페이스라고 한다.
	이 때 @FunctionalInterface를 인터페이스 위에 작성하여 단 하나의 추상 메소드만
	선언할 수 있도록 제한해야 한다.

#### 람다식(Lambda Expression)
	이름이 없는 메소드로서 값처럼 사용이 가능하며, 매개변수로도 전달이 가능하다.
	함수형 인터페이스는 추상 메소드가 한 개만 선언되기 때문에 메소드 이름이 필요 없다.
	따라서 람다식을 익명 메소드(Anonymous Method)라고도 부른다.

#### 람다식 문법
	1. (매개변수 형식 나열, ...) -> 리턴값;
	2. (매개변수 형식 나열, ...) -> { 2개 이상의 문장 작성; return 리턴값;}
	3. 소괄호 전부 생략 가능

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---------------------------------------------------------------------

#### 예외 처리
	컴파일 시, 빌드 시, 런타임 시 오류가 발생하면
	이를 제어문으로 막을 수 있으나, 제어문으로도 막을 수 없는
	오류들을 직접 처리할 수 있어야 한다.

#### 예외 처리 문법
	try {
		예외가 발생할 수 있는 문장

	} catch(예외이름 객체명){
		예외 발생 시 실행할 문장

	} catch(예외이름 객체명){
		예외 발생 시 실행할 문장

	} ...

	} finally {
		예외 발생 여부에 상관없이 무조건 실행할 문장
		※ 외부 장치와 연결했을 경우 다시 닫을 때 주로 사용한다.
	}

#### 예외 발생
	직접 예외를 발생시키기 위해서는 예외 던지기를 사용해야 하며, 이 때에는 생성자 호출 전 throw 키워드를 사용한다.
	예) throw new BadWordException();

#### 사용자 정의 예외
	기본적으로 제공되는 예외가 아닌 특정 상황에서 직접 예외를 만들어야 한다면, Exception 혹은
	RuntimeException을 상속받아서 예외 클래스를 선언해야 한다.
	Exception은 컴파일러가 체크를 하기 때문에 예외처리를 강제로 해야하고,
	RuntimeException은 컴파일러가 체크하지 않기 때문에 예외처리를 선택할 수 있다.
	
<p align="right">(<a href="#readme-top">back to top</a>)</p>

------------------------------------------------------------------------------------------------
#### API(Apllication Programming Interface)
	개발에 필요한 라이브러리들의 집합.
	선배 개발자들이 만들어 놓은 소스코드.

	- 내부 API
		JDK 설치 시 제공해주는 기본 API
		docs.oracle.com/javase

	- 외부 API
		선배 개발자들이 개발한 패키지 및 클래스들을 의미한다.
		보통 JAR파일로 배포하며 자바 프로젝트의 build path에 추가하여 사용할 수 있다.

#### JAR 파일로 배포하기
	배포할 클래스 또는 패키지 우클릭
	> Export > JAVA/JAR file 선택 > Next
	> destination을 원하는 경로로 선택
	> Export Java source files... 체크
	> Finish

#### JAR 파일을 프로젝트에 추가하기
	배포된 JAR파일을 다운 받기
	> 프로젝트 우클릭 > Build Path > Configure Build Path
	> Libraries 탭 클릭 > ClassPath(안되면 ModulePath) 클릭 > Add External JARs
	> 저장된 경로의 .jar파일을 더블 클릭으로 추가 > Apply 클릭
	> Orders and Exports 탭 클릭
	> Select All 클릭 > Apply and Close
	
<p align="right">(<a href="#readme-top">back to top</a>)</p>
  
----------------------------------------------------------------------------------------------

#### Object 클래스
	1. toString()
		항상 객체명을 출력할 때에는 toString()을 붙여서 출력해준다.
		따라서 객체명만 출력메소드에 전달하더라도 toString() 문자열 값이 출력된다.
		기본적으로 Object에서는 소속과 필드 주소를 문자열로 리턴해주지만,
		실사용에서는 불필요한 정보이기 때문에, 재정의한 뒤 필드의 정보를 확인하도록 구현한다.
		실무에서는 클래스 선언 시 각 필드의 초기화 여부를 확인하기 위해 toString()을 재정의하여 사용한다.

	2. equals()
		주소값 비교(==)
		String 클래스에서 equals()를 값 비교로 재정의하여 사용하기 때문에
		문자열 비교는 무조건 equals()로 비교한다.
		
	3. hashCode()
		JVM에서 관리하는 중복 없는 값. 실제 메모리에 할당되는 주소와 다르다.
		String 클래스에서는 필드의 해시코드 값이 아닌 문자열 상수값의 해시코드 값을
		리턴하도록 재정의하였다.
		※ 컬렉션 프레임워크 챕터에서 재정의 목적을 이해하도록 한다.
------------------------------------------------------------------------------------------------
#### Wrapper Class: 기본 자료형들의 클래스 타입
	클래스타입 객체 = new 클래스타입(일반타입의 값); //boxing, 권장하지 않는다(Deprecated).
	클래스타입 객체 = 클래스타입.valueOf(일반타입의 값); //boxing
	일반타입 변수 = 객체.000Value(); //unboxing

	JDK4버전 이상부터는 auto를 지원한다.

	클래스타입 객체 = 일반타입의 값; //auto boxing;
	일반타입 변수 = 객체; //auto unboxing;
-------------------------------------------------------------------------------------

#### 알고리즘
	어떤 문제가 발생되었을 때 해결할 수 있는 절차 혹은 순서.

#### 자료구조
	의미 없는 데이터를 하나의 정보로 만들어주는 알고리즘들의 집합.
	수집한 자료를 저장하는 방법.
	
<p align="right">(<a href="#readme-top">back to top</a>)</p>

#### 컬렉션 프레임워크(Collection Framework)
	많은 데이터를 쉽고 효과적으로 관리할 수 있는 표준화된 방법을 제공하는 클래스들의 집합.

##### 1. List extends Collection
	- Vector: 용량 관리, 보안성 강화, 처리량 감소
	- LinkedList: FILO로 인해 넣을 때는 빨라도 원하는 위치의 데이터를 가져오는 것이 상대적으로 느리다.
	- ArrayList: 인덱스로 데이터를 관리한다. 컬렉션 클래스 중 실무에서 가장 많이 사용되는 클래스이다.
		     배열의 특징인 인덱스를 이용하여 값을 저장하고 관리한다.

	※ 배열과 ArrayList의 차이
		배열은 길이에 제한을 두어야할 때 자주 사용되고,
		ArrayList는 몇 개의 데이터가 들어올 지 알 수 없을 때 사용한다.
    

----------------------------------------------------------------------------------------

##### 2. Set extends Collection
- 구현 클래스
	HashSet
		집합에서는 중복되는 원소를 포함할 수 없는 것 처럼
		HashSet이라는 자료구조는 중복되는 값을 무시한다.
		저장된 값들은 인덱스가 없기 때문에 순서가 없다.
		값의 유무 검사에 특화되어 있는 자료구조이고
		해시코드로 유무 검사가 진행되기 때문에 속도가 상대적으로 좋다.

- 순서 부여
	iterator()
	순서가 없는 객체에 순서를 부여하거나, 순서가 있어도 iterator방식의 순서로
	변경하고자 할 때 사용한다.
	hasNext()를 통해 다음 값이 있는 지 검사하고, next()를 사용해서 값을 가져온다.
  
----------------------------------------------------------------------------------------

##### 3. Map
- 구현 클래스
	HashMap(서버 간 데이터 교환)
		Key와 Value 한 쌍으로 저장되며, 검색의 목적을 가지고 있다.
		Key에 중복된 값을 중복된 값을 넣으면 Value가 최근 값으로 수정되고
		중복되지 않은 값을 넣으면 새롭게 추가된다. Value는 중복이 가능하다.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---------------------------------------------------------------------
#### 쓰레드

프로그램
	실행되지 않은 상태.

프로세스
	실행된 프로그램.

쓰레드
	프로세스 처리 경로.

	- 단일 쓰레드
		처리 경로를 한 개만 가지고 있기 때문에 직렬적이다.
		동시에 많은 양을 처리하기 힘들기 때문에 상대적으로 비효율적이다.
		하지만 하나의 작업에 문제가 발생하더라도 다른 작업에는 영향을 끼치지 않는다.
		따라서 안정성이 보장되고 설계 시 멀티 쓰레드에 비해 쉽다.

	- 멀티 쓰레드
		하나의 프로세스를 동시에 처리하는 것처럼 보이지만 사실은 매우 짧은 단위로 분할해서 차례로 처리한다.
		여러 개의 처리 경로를 가질 수 있도록 하며, 동시 작업이 가능해진다.
		설계하기 굉장히 어려우며, 하나의 쓰레드 문제 발생 시 모든 쓰레드에 문제가 발생하게 된다.
		JAVA 웹 서버가 대표적인 멀티 쓰레드이다. 멀티 쓰레드로 설계했다면, 처리량 증가, 효율성 증가,
		처리비용 감소의 장점이 있기 때문에 단점을 감수하고 설계하는 편이다.

멀티 쓰레드 구현 방법
	핵심 : run() 메소드 재정의

	1. Thread 클래스 상속
	2. Runnable 인터페이스 지정
-----------------------------------------------------------------------------------------

#### 동기화(Synchronized)
   하나의 쓰레드가 자원에 접근 중일 때 다른 쓰레드가 동시에 같은 자원을 접근하지 못하게 막는 것.
   즉, 자원 공유 문제를 해결할 수 있다.
   각 쓰레드를 제어해야 할 때에도 자주 사용된다.

##### 동기화 문법
   - 블럭: synchronized(mutex) {...}

   - 키워드: synchronized
      영역 전체에 동기화를 걸어주며, 메소드 리턴 타입 앞에 작성하면
      해당 메소드 전체에 동기화가 걸린다.

##### Thread 종료 방법
   1. 필드에 boolean 타입의 변수를 선언하고 run()안에 있는 반복문에 해당 변수가 true일 경우 break 하도록 설계한다.
   2. sleep() 또는 wait(), join() 등의 메소드를 통해 쓰레드 일시정지 상태일 경우
       Thread객체.interrupt()를 사용하여 InterruptedException을 발생시킨다.
       이 때 일시정지 시킨 메소드 부분의 catch를 통해 예외를 잡아주고 원하는 문장을 작성하면 된다.
   3. 쓰레드를 일시정지하는 코드가 없을 경우 Thread.interrupted()의 상태를 확인한다.
       Thread객체.interrupt() 사용 시 Thread.interrupted()의 상태는 true로 변경된다.
            권장하지 않는 방법이다.
   4. System.exit(0)를 사용하면 전체 쓰레드 종료(프로세스 종료)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---------------------------------------------------------------------
#### 파일 입출력( Java Application 관점 )
	Stream 이라는 연결통로를 통해 원본 데이터가 알맞는 인코딩 방식으로 전송된다.
	byte단위로 입출력되기 때문에 개별처리이며, 상세 연산이 필요하지 않다면 Buffer를 사용한 입출력을 권장한다. Buffer를 사용하면 일괄처리가 가능해진다.
	Stream -> 용량이 큰거
	Buffer -> 용량이 작은거

※ 인코딩 방식	
	인코딩 방식은 완성형과 조합형이 있다.
	- 완성형 : 각, 간, 갈, 감, ...., 갛 ...
	- 조합형 : ㄱ + ㅏ + ㄱ
	
조합형이 효율적이며 byte 단위로 데이터를 전송할 때 고정된 byte가 아니기 때문에 가변형 인코딩 방식을 선호한다. 조합형이면서 가변형인 인코딩 방식은 UTF-8이며, 전 세계에서 가장 많이 사용되는 방식이다.


##### writer (출력) 
	BufferWriter : 버퍼를 사용한 출력 클래스
	FileWriter : 전달한 경로의 파일을 출력하기 위한 목적으로 열어준다.
	전달한 경로에 파일이 없다면 새롭게 만든 후 열어준다.
	객체화를 하면 파일이 열린다.


##### Reader (입력)
	BufferedReader : 버퍼를 사용한 입력 클래스
	FileReader : 전달한 경로의 파일을 입력하기 위한 목적으로 열어준다.
	전달한 경로에 파일이 없다면 FileNotFoundException이 발생한다.

##### File (파일 정보)
	전달한 경로에 있는 파일의 정보를 담는 타입.
	디렉터리 생성, 해당 경로의 전체 파일 목록, 파일 삭제 등
	
<img width="1000" src="https://github.com/code-hyun/study-java/assets/122762287/c7db3568-b70b-4f32-8507-ce627208b461">


<p align="right">(<a href="#readme-top">back to top</a>)</p>

----------------------------------------------------------------------------------------------------------------------------

#### 소프트웨어 디자인 설계 패턴

##### ▶ MVC
   M(Model): DB에서 조회된 결과 값을 담기 위한 변수들이 선언된 클래스
        - 클래스명 뒤에 VO, DTO라는 문자열을 붙여준다.
        - VO(Value Object): 테이블을 보고 그대로 만든 객체
        - DTO(Data Transfer Object): 화면에 필요한 데이터를 담은 객체
	-domain


   V(View): 사용자에게 보여질 화면을 구성하는 부분

   C(Controller): DB에 접근할 수 있는 메소드들이 선언된 클래스
         - 접근 후 결과 값이 있을 경우 Model 객체에 담은 후 처리
         - 클래스명 뒤에 DAO라는 문자열을 붙여준다.
         - DAO(Data Access Obejct)


<p align="right">(<a href="#readme-top">back to top</a>)</p>
