클린파이썬을 공부하며 정리하여 업로드하는 REPO입니다.

# 1장 요약

- 함수와 변수의 이름은 소문자로, 또한 밑줄로 구분된 단어로 지정.

```python
names = 'Python' # 변수이름
job_title = 'Software Engineer' # 밑줄로 구분한 변수
popilated_countries_list  = [] #밑줄로 구분한 변수 
```

- 함수나 변수에 기능을 내포할 수 있는 이름 사용
```python
#사용자 ID가 제공되는 경우 user 객체를 반환 하는 함수

# 잘못된 방법
def get_user_info(id):
    db = get_db_connection()
    user = execute_query_for_user(id)
    return user

# 올바른 방법
def get_user_by(user_id):
    db = get_db_connection()
    user = execute_query_for_user(id)
    return user
```

- 클래스의 이름은 `Camel Case`로
- 상수 이름은 대문자로
- ''.join(['abc','def]) 활용 -> 가독성및 빠른 속도 보장
- 람다식 사용 자제
- 함수 작성 시 모든 경우를 생각해 return 작성.
- 두 객체 타입을 비교할때 `type()` 대신 `isinstance()` 사용
- boolen 값을 비교할 때
```python
# 추천하지 않는 방법
if is_empty == False:
if is_empty is False

# 추천하는 방법

if is_empty :
```
- 함수 사용시 독스트링 작성
```python
def call_weather_api(url: str, location: str) -> str:
"""특정 위치의 날씨를 얻는다.  

날씨 API와 위치를 사용해 날씨를 확인하고자 날씨 API를 호출한다.
도시 이름만 제공할 수 있도록 하고, 국가 및 카운티 이름은 
허용되지 않을 것이며 도시 이름을 찾이 못하면 예외를 발생시킬 것이다.
```

- 클래스 독스트링 
```python
class Student:
    """Student 클래스 정보 

    이 클래스는 학생이 수행한 작업을 처리한다.
    이 클래스는 학생의 성명, 나이, 전화번호와 기타 정보를 제공한다.

    사용법:
    import student

    student = student.Student()
    student.get_name()
    >> 678988
    """

    def __init__(self)
    pass
```

- 복잡하지 않은선에서 리스트 컴프리헨션 사용
- 파일의 메모리 크기가 확실하지 않으면 이터레이터 사용
```python
# 이터레이터 사용
def read_file(file_name):
    """Read the file line by line."""
    with open(file_name) as fread:
        for line in fread:
            yield line


for line in read_file("logfile.txt"):
    print(line.startswith(">>")
```

- 예외를 포착하는 동안 `except:` 절을 사용하는 대신 특정 예외만 잡는 것을 추천함.  
- 예외 발생시 None 반환 지양
```python
# 추천 하는 방법 
def get_even_list(num_list):
    """지정된 리스트에서 짝수 리스트를 얻는다."""
    #NoneType 또는 TypeError 예외를 발생시킬 수 있다.
    return [item for item in num_list if item%2==0]

numbers = None
try : 
    get_even_list(numbers)
except TypeError:
    print("Type error has been raised due to non sequential data type.")

```

# 2장 요약
- 리스트 사용시 메모리 이슈 주의
- 제너레이터로 쓰는 습관.
```python
import math

def is_prime(num):
    prime = True
    for item in range(2, int(math.sqrt(num)) + 1):
        if num % item == 0:
            prime = False
    return prime
    
def get_prime_numbers(lower, higher):
    for possible_prime in range(lower, higher):
        if is_prime(possible_prime):
            yield possible_prime
        yield False

for prime in get_prime_numbers(30, 50):
    if prime:
        print(prime)
```
- 두개의 리스트를 병렬적으로 처리해야 한다면 zip 사용.
- 카운터: 카운터는 유사한 데이터를 집계할 수 있는 편리한 방법을 제공한다.  

```python
from collections import Counter

contries  = ["Belarus", "Albania", "Malta", "Ukrain", "Belarus", "Malta", "Kosove", "Belarus"]
Counter(contries)
"""
>>> Counter({'Belarus': 3, 'Malta': 2, 'Albania': 1, 'Ukrain': 1, 'Kosove': 1})
"""
```
- deque : 큐와 스택을 생성하려면 deque를 사용하면 됨.
- defaultdict :  defaultdict는 dict와 같은 KeyError을 발생시키지 않는다. 존재하지 않는 키는 기본 값을 반환한다.
- 두개의 딕셔너리 병합 하기 
```python
salary_first = {"Lisa": 238900, "Ganesh": 8765000, "John": 3450000}
salary_second = {"Albert": 3456000, "Arya": 987600}
{**salary_first, **salary_second}

>>{"Lisa": 238900, "Ganesh": 8765000, "John": 3450000,"Albert": 3456000, "Arya": 987600}
```



# 3장 요약
- 함수 작성시 하나의 작업만 수행하도록 작성.
- None을 반환하는 대신 예외 발생
- default 및 keyward argument 를 사용한 동작 추가.
```python
spam_emails(from = 'ab_from@gmail.com',to = 'nb_to@naver.com',subject= 'is email spam',size = 10000,to = 'an',from = 'bd')
 ```
- 명시적인 None 반환 금지.
```python
# 아래 코드는 기본적으로 None를 반환한다.
# 좋지 않은 사례
def sum(first_number, second_number):
    sum = first_number + second_number

sum(80,90)
```
- 방어적인 함수 작성 : 로깅, 단위 테스트
- 선호되는 클래스 구조
    1. 클래스 변수
    2. __init__
    3. 내장 파이썬 특수 메서드(__call__, __repr__등)
    4. 클래스 메서드
    5. 정적 메서드
    6. 속성
    7. 인스턴스 메서드
    8. 프라이빗 메서드 

- 정적 메소드 사용 시기 : 클래스 내부에 메서드를 유지하면 해당 함수를 클래스와 쉽게 연관시킬 수 있을때
- private 메소드 대신 public 속성 사용
```python
class Person:
    def __init__(self, first_name, last_name):
        self.age = 50
        self.full_name = first_name + last_name

    def get_name(self):
        return self.full_name

class Child(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.__age = 20


ch = Child("Larry", "Page")
print(ch.age)              # 50
print(ch._Child__age)      # 20
```