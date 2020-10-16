## ndarray 생성


```python
import numpy as np

list1 = [1,2,3]
print('list1 :  ',list1)
print('list1 type',type(list1))
array1 = np.array(list1)
print('array1 : ',array1)
print('array1 type',type(array1))
```

    list1 :   [1, 2, 3]
    list1 type <class 'list'>
    array1 :  [1 2 3]
    array1 type <class 'numpy.ndarray'>
    


```python
array1 = np.array([1,2,3])
print('array1 type:' ,type(array1))
print('array1 array 형태',array1.shape)

array2 = np.array([[1,2,3],
                   [4,5,6]])
print('array1 type:' ,type(array2))
print('array1 array 형태',array2.shape)

array3 = np.array([[1,2,3]])
print('array3 type:' ,type(array3))
print('array3 array 형태',array3.shape)
```

    array1 type: <class 'numpy.ndarray'>
    array1 array 형태 (3,)
    array1 type: <class 'numpy.ndarray'>
    array1 array 형태 (2, 3)
    array3 type: <class 'numpy.ndarray'>
    array3 array 형태 (1, 3)
    


```python
print('arr1의 차원: {0} arr2의 차원: {1} arr3의 차원: {2}'.format(array1.ndim,array2.ndim,array3.ndim))
```

    arr1의 차원: 1 arr2의 차원: 2 arr3의 차원: 2
    


```python
# ndarray 데이터 값 타입
list1 = [1, 2, 3]
print(type(list1))
array1 = np.array(list1)

print(type(array1))
print(array1, array1.dtype)
```

    <class 'list'>
    <class 'numpy.ndarray'>
    [1 2 3] int32
    


```python
list2 = [1,2,'test']
array2 =np.array(list2)
print(array2, array2.dtype)

list3= [1,2,3.0]
array3 = np.array(list3)
print(array3, array3.dtype)
```

    ['1' '2' 'test'] <U11
    [1. 2. 3.] float64
    

## ndarray 타입 변환
---
`astype()를 이용하여 변환` 
    - 변경을 원하는 타입을 astype() 에 인자로 입력
    - 대용량 데이터를 ndarray로 만들 때 메모리를 절약하기 위해 자주 사용.
    


```python
array_int = np.array([[1,2,3]])
array_float = array_int.astype('float64')
print(array_float, array_float.dtype)

array_int1 = array_float.astype('int32')
print(array_int1, array_int1.dtype)

array_float1 = np.array([1,2.1,3.1])
array_int2 = array_float1.astype('int32')
print(array_int2, array_int2.dtype)
```

    [[1. 2. 3.]] float64
    [[1 2 3]] int32
    [1 2 3] int32
    

## 넘파이 ndarray의 axis 축
---
![image.png](attachment:image.png)


```python
# ndarray에서 axis 기반의 연산함수 수행

array2 = np.array([[1, 2, 3], [2, 3, 4]])

print(array2.sum())
print(array2.sum(axis=0))
print(array2.sum(axis=1))
```

    15
    [3 5 7]
    [6 9]
    

# ndarray를 편하게생성하기 - arrange , zeros,ones
---


```python
print(np.arange(10))
print(np.zeros((3,2),dtype='int32'))
print(np.ones((3,2)))
```

    [0 1 2 3 4 5 6 7 8 9]
    [[0 0]
     [0 0]
     [0 0]]
    [[1. 1.]
     [1. 1.]
     [1. 1.]]
    

# ndarray의 차원과  크기를  변경하는 reshape()
---
- reshape(-1,5) 와 같이 인자에 -1 을 부여하면 -1에 해당하는 axis의 크기는 가변적으로 변한다


```python
array1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(array1)
print(array1.reshape(2,5))
print(array1.reshape(5,-1)) # 여기서는 -1이 2로 변함
```

    [0 1 2 3 4 5 6 7 8 9]
    [[0 1 2 3 4]
     [5 6 7 8 9]]
    [[0 1]
     [2 3]
     [4 5]
     [6 7]
     [8 9]]
    

#  인덱싱
---

- 단일  값 추출


```python
array1 = np.arange(start=1,stop=10)
print('array1:',array1)

value = array1[2]
print('values:', value)
print(type(value))
```

    array1: [1 2 3 4 5 6 7 8 9]
    values: 3
    <class 'numpy.int32'>
    


```python
array1[0]=9
array1[8]=0
print('array1:',array1)
```

    array1: [9 2 3 4 5 6 7 8 0]
    

- 슬라이싱


```python
array1 = np.arange(start=1,stop=10)
array3=  array1[0:3]
print(array3)
print(type(array3))
```

    [1 2 3]
    <class 'numpy.ndarray'>
    


```python
array1d = np.arange(start=1, stop=10)
array2d = array1d.reshape(3,3)
print('array2d:\n',array2d)

print('array2d[0:2, 0:2] \n', array2d[0:2, 0:2])
print('array2d[1:3, 0:3] \n', array2d[1:3, 0:3])
print('array2d[1:3, :] \n', array2d[1:3, :])
print('array2d[:, :] \n', array2d[:, :])
print('array2d[:2, 1:] \n', array2d[:2, 1:])
print('array2d[:2, 0] \n', array2d[:2, 0])
```

    array2d:
     [[1 2 3]
     [4 5 6]
     [7 8 9]]
    array2d[0:2, 0:2] 
     [[1 2]
     [4 5]]
    array2d[1:3, 0:3] 
     [[4 5 6]
     [7 8 9]]
    array2d[1:3, :] 
     [[4 5 6]
     [7 8 9]]
    array2d[:, :] 
     [[1 2 3]
     [4 5 6]
     [7 8 9]]
    array2d[:2, 1:] 
     [[2 3]
     [5 6]]
    array2d[:2, 0] 
     [1 4]
    

- fancy indexing


```python
array1d = np.arange(start=1, stop=10)
array2d = array1d.reshape(3,3)

array3 = array2d[[0,1], 2]
print('array2d[[0,1], 2] => ',array3.tolist())

array4 = array2d[[0,1], 0:2]
print('array2d[[0,1], 0:2] => ',array4.tolist())

array5 = array2d[[0,1]]
print('array2d[[0,1]] => ',array5.tolist())
```

    array2d[[0,1], 2] =>  [3, 6]
    array2d[[0,1], 0:2] =>  [[1, 2], [4, 5]]
    array2d[[0,1]] =>  [[1, 2, 3], [4, 5, 6]]
    

- boolean indexing


```python
array1d = np.arange(start=1,stop=10)

array3 = array1d[array1d >5]
print('array1d > 5  불린 인덱싱 결과 값  : ',array3)
```

    array1d > 5  불린 인덱싱 결과 값  :  [6 7 8 9]
    


```python
array1d > 5
```




    array([False, False, False, False, False,  True,  True,  True,  True])



# 배열의 정렬 - sort()와 argsort()


## sort()
- np.sort() : 원 행렬은 그대로 유지한 채 원 행렬의 정렬된 행렬을 반환
- ndarray.sort() 원 행렬 자체를 정렬한 형태로 변화하며 반환 값은 None



```python
org_array = np.array([3, 1, 9, 5])
print('원본 행렬:', org_array)

# np.sort( )로 정렬
sort_array1 = np.sort(org_array)
print('np.sort( ) 호출 후 반환된 정렬 행렬:', sort_array1)
print('np.sort( ) 호출 후 원본 행렬:', org_array)

# ndarray.sort( )로 정렬
sort_array2 = org_array.sort()
print('org_array.sort( ) 호출 후 반환된 행렬:', sort_array2)
print('org_array.sort( ) 호출 후 원본 행렬:', org_array)
```

    원본 행렬: [3 1 9 5]
    np.sort( ) 호출 후 반환된 정렬 행렬: [1 3 5 9]
    np.sort( ) 호출 후 원본 행렬: [3 1 9 5]
    org_array.sort( ) 호출 후 반환된 행렬: None
    org_array.sort( ) 호출 후 원본 행렬: [1 3 5 9]
    


```python
# 내림차 순 정렬
sort_arr_desc = np.sort(org_array)[::-1]
print('내림차순 정렬 : ',sort_arr_desc)
```

    내림차순 정렬 :  [9 5 3 1]
    

### 2차원 배열에서 axis 기반의 sort()



```python
arr = np.array([[8, 12], [7, 1]])
print(arr)
print(np.sort(arr, axis=0))
print(np.sort(arr, axis=1))
```

    [[ 8 12]
     [ 7  1]]
    [[ 7  1]
     [ 8 12]]
    [[ 8 12]
     [ 1  7]]
    

## argsort()
-  원본행렬 정렬 시 정렬된 행렬의 원래   인덱스를 필요로 할때 np.argsort()를 이용.
np.argsort()는 정렬 행렬의 원본 행렬 인덱스를  ndarray를  형으로 반환
![image.png](attachment:image.png)


```python
org_array = np.array([ 3, 1, 9, 5]) 
sort_indices = np.argsort(org_array)
print(type(sort_indices))
print('행렬 정렬 시 원본 행렬의 인덱스:', sort_indices)
```

    <class 'numpy.ndarray'>
    행렬 정렬 시 원본 행렬의 인덱스: [1 0 3 2]
    


```python
import  numpy as np

name_array = np.array(['John', 'Mike', 'Sarah', 'Kate', 'Samuel'])
score_array= np.array([78, 95, 84, 98, 100])

sort_indices_asc = np.argsort(score_array)
print('성적 오름차순 정렬 시 score_array의 인덱스:', sort_indices_asc)
print('성적 오름차순으로 name_array의 이름 출력:', name_array[sort_indices_asc])
```

    성적 오름차순 정렬 시 score_array의 인덱스: [0 2 1 3 4]
    성적 오름차순으로 name_array의 이름 출력: ['John' 'Sarah' 'Mike' 'Kate' 'Samuel']
    

## 선형대수  연산 - 행렬 내적
---
`np.dot(A,B)`
![image.png](attachment:image.png)


```python
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

dot_product = np.dot(A,B)
print('행렬 내적 결과 : \n',dot_product)
```

    행렬 내적 결과 : 
     [[ 58  64]
     [139 154]]
    

## 선형대수 연산 - 전치행렬



```python
A = np.array([[1, 2],
              [3, 4]])
A_trans = np.transpose(A)
print('A의 전치 행렬:\n',A_trans)
```

    A의 전치 행렬:
     [[1 3]
     [2 4]]
    
