## PEP 8 이란 무엇인가?!

**PEP 8은 "Style Guide for Python Code"로 파이썬 코드를 어떻게 구상해야할 지 알려주는 스타일 가이드**입니다. 

PEP 8은 파이썬 구문의 많은 특수성(다른 언어에서 일반적으로 적용되지 않는)을 고려하여 작성되었습니다.

## PEP 8을 왜 따라야 하나?!

1. 일관성
    
    **코드가 일정한 포맷을 가지면 훨씬 쉽게 읽을 수 있습니다.**
    
    신규 입사자 교육 시에 매우 중요한 부분이기도 합니다. 새로운 개발자나 경험이 많지 않은 개발자를 채용한 경우에도 여러 저장소의 코드에 익숙해야합니다.
    
    이 때 레이아웃, 문서화, 이름 작명 규칙 등의 모든 저장소에서 동일하다면 훨씬 쉽게 익숙해질 것입니다.
    
2. 코드 품질
    
    **코드를 구조화하여 살펴보면 한 눈에 코드를 이해하고 버그와 실수를 쉽게 찾을 수 있습니다.**
     이 외에도 코드 품질 도구를 사용하면 잠재적인 버그를 찾을 수도 있습니다.
    

---

## **들여쓰기 (Indentation)**

들여쓰기는 4개의 스페이스를 사용해야 합니다.

한 줄의 코드를 여러줄로 나눠 쓰는 경우 다음 사항을 고려해야 합니다.

- 첫번째 줄에 인자가 있으면 수직정렬하여 읽기 좋게 만듭니다.
- 첫번째 줄에 인자가 없다면, 추가로 들여쓰기를 하여 다음행과 구별이 되도록 해야 합니다.

### 좋은 예

```python
# 첫번째 줄에 인자가 있으면 수직정렬을 하여 인자들을 보기 좋게 합니다.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# 첫번째 줄에 인자가 없다면, 한번 더 들여쓰기(4개의 스페이스)하여 다음행과 구분이 되도록 합니다.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# 여러줄로 나눠쓰는 경우 다음행과 구분이 되도록 들여쓰기를 합니다.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```

### 나쁜 예

```python
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# 한줄을 여러줄로 나눠쓰는 경우 추가로 들여쓰기를 하지 않으면 안됩니다. 다음행과 구분이 어렵습니다.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

### 선택 사항

`{}`, `()`, `[]`를 사용할 때,

 괄호를 닫을때는 마지막 줄에 맞추거나, 첫번째 줄에 맞춰서 닫으면 됩니다.

```python
# 마지막 줄의 첫번째 아이템에 정렬하여 괄호를 닫은 경우
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )

# 첫번째 줄에 정렬하여 괄호를 닫은 경우
my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
```

## **Line 최대 길이**

코드 한줄은 79자 이내로 작성하기를 권장합니다.

모니터가 커서 한눈에 다 보일 수 있지만 Opensource 프로젝트처럼 불특정 다수에게 보여지는 코드라면 79자 규칙을 지키는게 좋습니다.

코드가 길어지는 경우 백슬러시(`\`)를 이용해서 줄바꿈을 하면 됩니다.

```python
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```

특히 연산자들로 인해 길게 늘어지는 경우, 연산자가 앞에 오도록 줄바꿈하는 것이 좋습니다.

### 좋은예

```python
# 연산자 앞에 있는 경우 코드 가독성이 좋음
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

### 나쁜예

```python
# 연산자 이후에 줄바굼하여 이어지는 코드를 보기 어려움
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
```

## Blank Lines

빈 줄은 클래스 또는 함수간의 정의를 구분할 때 사용하고, 코드 내에 연관성이 있는 코드 덩어리를 묶는데 사용됩니다.

- 최상위 클래스 또는 함수들의 정의를 구분할 때는 두 줄 띄워 구분합니다.
- 클래스 내에 정의한 메소드들은 한 줄을 띄워 구분합니다.
- 함수 내에 연관성 있는 코드 덩어리를 구분할 때 빈 줄을 사용할 수 있습니다.

```python
def get_extractor():
  pass

class YoutubePlaylistsBaseInfoExtractor(YoutubeEntryListBaseInfoExtractor):

    def _process_page(self, content):
        pass

    def _real_extract(self, url):
        pass

class YoutubeIE(YoutubeBaseInfoExtractor):

    def _real_extract(self, url):
        pass
```

## **Source File Encoding**

파일의 인코딩은 항상 UTF-8을 사용합니다.(Python 2에서는 ASCII)

Python3의 기본 인코딩은 UTF-8입니다. UTF-8을 사용한다면 인코딩을 따로 명시할 필요가 없습니다. (Python 2에서는 ASCII가 기본)

## **Imports**

한 줄에 두개의 모듈을 임포트하는 것은 바람직하지 않습니다.

### 나쁜 예

```python
import sys, os
```

한줄에 1개의 모듈만 Import하는 것을 권장하고, `from`으로 동일한 곳에서 여러 모듈을 Import할 때는 한 줄로 사용할 수 있습니다.

### 좋은 예

```python
import sys

from subprocess import Popen, PIPE
```

Import는 항상 파일의 맨 위에 작성해야 하며, 다음 그룹들을 분류하여 정의하는 것을 권장합니다.

- Standard library imports
- 3rd party library imports
- Local application/library specific imports

이 그룹들 간에는 빈 줄 하나를 넣어 서로 구분되도록 해야 합니다.

그리고 절대경로를 이용하여 Import하는 것이 권장됩니다. (절대 경로가 너무 비효율적일 때 는 상대경로로 작성해도 됨.)

```python
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example
```

모듈 안에 있는 클래스를 Import할 때는 아래 처럼 사용할 수 있습니다.

```python
from myclass import MyClass
from foo.bar.yourclass import YourClass
```

만약 동일 이름의 클래스가 있어 충돌이 발생하는 경우, 모듈을 먼저 Import하고 코드에서는 `myclass.MyClass` 와 같은 식으로 사용할 수 있습니다.

```python
import myclass
import foo.bar.yourclass

a = myclasss.MyClass
```

모듈 import 시 wildcard(*)를 사용하는 방식은 최대한 자제해야 합니다. 매우 불명확하고 코드 가독성을 저해합니다.

```python
from <module> import *
```

## **Dunders Names**

`__all__`, `__author__`, `__version__` 와 같이 단어 앞 뒤로 더블 언더스코어(__)를 사용하는 것을 Dunders name라고 한다. all, vesion 같은 경우 파이썬에서 특수 용도로 예약 되어있고, 버전이 바뀌면서 수정될 수 이기때문에 사용 하지 않는 것이 바람직하며 그렇기 때문에 더블 언더스코어로 구분해주는 것입니다.

Dunders Names 정의는 모듈의 docstring과 import 코드 사이에 위치하는 것을 권장합니다.

특별히 `from __future__ import barry_as_FLUFL` 코드는 import 코드에서 예외로 합니다.(barry_as_FLUFL는 `<>`를 `!=`로 사용할 수 있는 것이라고 합니다(?))

```python
"""This is the example module.

This module does stuff.
"""

from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys
```

## **따옴표("" 또는 '')**

파이썬에서는 ''와 ""로 생성된 문자열을 따로 구분하지 않습니다. 모두 동일하게 취급됩니다. 그리고 PEP에서도 따로 어떤 것을 쓰라고 권유하지 않습니다. 하지만 따옴표 내부에 따옴표를 사용해야 하는 경우 서로 다른 따옴표를 사용해야 한다 그러면 가독성을 해치는 백슬러시(\)를 사용하지 않을 수 있습니다.

docstring에 사용되는 따옴표 3개는 꼭 두개짜리 따옴표(")를 사용해주세요!!  docstring의 일관성을 유지하기 위함.. 이라고 합니다.

```python
"""This is the example module.

This module does stuff.
"""
```

## **Whitespace in Expressions and Statesment**

Expression은 `1+1`과 같은 수식을, Statesment는 코드 한줄을 의미합니다. Statesment는 Expression을 포함할 수도 있습니다. 이런 코드 안에서 띄어쓰기를 어떻게 할지에 대한 가이드라인입니다.

의미없는 띄어쓰기는 하지마세요.

괄호에 붙어있는 코드를 띄울 필요는 없습니다.

```python
Yes: spam(ham[1], {eggs: 2})
No:  spam( ham[ 1 ], { eggs: 2 } )
```

Comma(,)와 닫는 괄호 사이를 띄울 필요는 없습니다.

```python
Yes: foo = (0,)
No:  bar = (0, )
```

`:` 사이는 띄울 필요는 없지만, 수식이나 함수가 들어갔을 때 띄우는 것이 좋습니다. `:`
의 양 옆의 공백이 동일하도록 해야 합니다. 하지만 `:`에 인자가 없다면 띄울 필요가 없습니다.

```python
# 좋은 예:
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]

# 나쁜 예:
ham[lower + offset:upper + offset]
ham[1: 9], ham[1 :9], ham[1:9 :3]
ham[lower : : upper]
ham[ : upper]
```

여는 괄호 직전에 띄우지 않습니다.

```python
Yes: spam(1)
No:  spam (1)
```

또한, dict의 경우도 여는 괄호 직전에 띄우지 않습니다.

```python
Yes: dct['key'] = lst[index]
No:  dct ['key'] = lst [index]
```

변수 선언 및 할당할 때 한칸씩만 띄워주면 됩니다. 줄을 맞추기 위해 과도하게 띄어쓰기를 사용할 필요는 없습니다.

```python
# 좋은 예:
x = 1
y = 2
long_variable = 3

# 나쁜 예:
x             = 1
y             = 2
long_variable = 3
```

## **Other Recommendations**

할당(=), 증감연산자(+=, -=), 비교연산자(==, <, >, !=, <>, <=, >=, in, not in, is, is not), Boolean연산자(and, or, not)를 사용할 때 스페이스 한칸씩 넣어주세요.

우선순위가 다른 연산자들을 함께 쓸 때, 우선순위가 가장 낮은 연산자 주위로 스페이스 한칸씩 넣어 구분을 해주세요. 어떤게 먼저 연산이 되는지 읽기 쉬워집니다.

```python
# 좋은 예:
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)

# 나쁜 예:
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
```

Function annotations을 사용한다면, `:`과 `->`를 사용할 때 아래처럼 스페이스를 넣어주어야 합니다.

```python
# 좋은 예:
def munge(input: AnyStr): ...
def munge() -> AnyStr: ...

# 나쁜 예:
def munge(input:AnyStr): ...
def munge()->PosInt: ...
```

Function annotations을 사용하지 않는다면, default value를 설정할 때 `=` 사이를 띄우면 안됩니다.

```python
# 좋은 예:
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# 나쁜 예:
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)
```

Function annotations과 default value를 섞어서 사용할 때는 아래처럼 `=`와 `:` 사이를 띄워주세요.

```python
# 좋은 예
def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...

# 안좋은 예
# Wrong:
def munge(input: AnyStr=None): ...
def munge(input: AnyStr, limit = 1000): ...
```

코드 한줄에 여러개의 명령문을 넣지마세요.

```python
# 좋은 예:
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()

# 나쁜 예:
if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()

# 권장하진 않지만,
# if나 for, while을 사용하여 한줄로 표현할 수 있는 코드라면 상황을 보고 한줄로 표현하세요.
if foo == 'blah': do_blah_thing()
for x in lst: total += x
while t < 10: t = delay()

# 하지만 이런 코드들은 절대 권장하지 않습니다.
if foo == 'blah': do_blah_thing()
else: do_non_blah_thing()

try: something()
finally: cleanup()

do_one(); do_two(); do_three(long, argument,
                             list, like, this)

if foo == 'blah': one(); two(); three()
```

## **주석**

- 이상한 주석은 없는 것 만 못합니다. 주석을 넣기로 결정했으면 코드가 변할 때마다 주석도 변화에 맞게 변경되어야 합니다.
- 주석의 첫 글자는 대문자로 시작해야 합니다. 예외적으로, 식별자(identifier)가 소문자로 시작한다면 소문자를 사용해야 합니다.
- 작성한 코드가 비영어권자만 읽는 코드가 아니라면, 꼭 영어로 작성해주세요.
- Inline comment(코드와 같은 라인에 사용하는 주석)는 적게 사용해주세요. Inline comment는 불필요하고 보기 힘들 때가 많습니다.

## **Documentation string**

docstring에 대한 컨벤션은 [PEP 257](https://www.python.org/dev/peps/pep-0257/)을 참고하시면 됩니다.

중요한 것은, 여러줄로 docstring을 작성할 때 마지막 `"""`은 마지막줄에 홀로 사용되도록 해야 합니다. 만약 한줄인 docstring은 동일 라인에 `"""`를 사용해야 합니다.

```python
# 좋은 예:
"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.
"""

"""Return a foobang"""

```

## **Naming convention**

leading underscores**(앞에 있는 _)**와 trailing underscores**(뒤에 있는 _)**를 파이썬에서 사용할 때 다음과 같이 사용할 수 있습니다. 각각의 의미와 동작 결과는 아래와 같습니다. 코딩을하면서 이름지을 때는 single leading underscore와 single trailing underscore만 사용하는 것이 좋을 것 같습니다.

- _single_leading_underscore : **내부적으로 사용하는 변수를 의미할 때** 앞에 언더스코어(_)를 넣습니다
- single_trailing_underscore_ : **파이썬에서 기본 키워드와 겹치는 것을 피하려면** 마지막에 언더스코어를 넣습니다.
- __double_leading_underscore : 더블 언더스코어(__)는 name mangling과 관련된 것입니다.

만약 __method라고 이름을 지으면 name mangling에 의해 _ClassName__method로 변경됩니다. 이름이 변경되기 때문에 ClassName.__method로 접근할 수 없습니다. **그래서 일반적인 경우로는 사용하지 않는 것이 좋습니다.**

- __double_leading_and_trailing_underscore__ : Magic 객체라고 합니다.

예를들어 __init__ 또는 __import__ 또는 __file__ 등이 있습니다. 이런식으로 이름을 만들지 말고 기존에 정의된 것만 사용해야 합니다.

### **이름지을 때 피해야 할 문자**

한글자로 변수명을 지을 때 'l' (lowercase letter el), 'O' (uppercase letter oh), 'I' (uppercase letter eye) 는 피해야 합니다. Font에 따라서 숫자 0인지 알파벳 O인지 구분이 안되는 경우가 있기 때문입니다.

### **ASCII Compatibility**

standard library 내에서 사용되는 변수의 이름은 ASCII와 호환가능한 문자로 지어져야 합니다.

### **Class Names**

클래스의 이름은 CapWords(CamelCase) 규칙으로 짓습니다.

### **Exception Names**

클래스와 동일하게 CamelCase로 짓습니다. 하지만 Error를 접미사로 붙여야 합니다.(예외가 실제로 Error인 경우에만 해당됩니다.)

### **Global Variable Names**

모듈 내부적으로만 사용하는 변수라면, 함수 네이밍 규칙과 비슷합니다.

밖으로 쉽게 보이지 않도록 Import로만 글로벌 변수를 사용하게 하고 싶다면, __all__ 매커니즘을 이용할 수 있습니다. 또는 언더스코어를 앞에 붙여 모듈 내부적으로만 사용하는 변수라는 의미를 부여할 수 있습니다.

### **Function and Variable Names**

함수 이름은 소문자로 작성하며, 단어 사이를 언더스코어(_)로 구분해줍니다.

### **Function and Method Arguments**

instance 메소드의 첫번째 인자 이름은 `self`를 사용해야 합니다. class 메소드의 첫번째 인자 이름은 `cls`를 사용해야 합니다.

만약 다른 코드와 이름이 동일하여 충돌이 발생하는 경우 이름 뒤에 언더스코어를 넣어 충돌을 피할 수 있습니다. 이름을 모호하게 변경하는 것보다 언더스코어를 뒤에 붙여주는 것이 좋을 때가 많습니다.

### **Constants**

상수는 보통 모듈 수준에서 정의됩니다. 모두 대문자를 사용하며 언더스코어로 단어 간의 구분을 합니다. 예를들어, MAX_OVERFLOW, TOTAL와 같이 이름을 지을 수 있습니다.

## ****Programming Recommendations****

접두사, 집머사를 비교할 때는 string slicing을 사용하지 말고 startwith(), endwith()를 사용하는 것이 의미상 명확합니다. 

```python
# 좋은 예:
if foo.startswith('bar'):

# 나쁜 예:
if foo[:3] == 'bar':
```

데이터 타입을 비교할 때는 직접 비교하기보다 isinstance()를 사용하는 것이 좋다.

```python
# 좋은 예:
if isinstance(obj, int):

# 나쁜 예:
if type(obj) is type(1):
```

문자열, 리스트, 튜플 등이 비어있는지 체크하려면 len을 사용하지 말고 if에 직접 넣어 확인하는게 좋다.

```python
# 좋은 예:
if not seq:
if seq:

# 나쁜 예:
if len(seq):
if not len(seq):
```

None과 같은 싱글턴 객체를 비교할 때는 `is` 또는 `is not`을 사용하세요.

절대로 `==`와 같은 equality 연산자를 사용하시면 안됩니다. (동등성(equality)을 비교할 때만 `==` 또는 `!=`와 같은 equality 연산자를 사용하세요)

그리고 boolean을 비교할 때는 `==`도 사용하지 마세요. 비교하지 말고 객체 자체의 True, False를 사용하세요.

```python
Yes:   if greeting:
No:    if greeting == True:
Worse: if greeting is True:
```
