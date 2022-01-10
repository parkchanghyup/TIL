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

# 3장 요약
