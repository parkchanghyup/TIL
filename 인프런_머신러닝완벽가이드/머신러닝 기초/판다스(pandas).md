# 판다스
---
- 행과 열로 이뤄진 2차원 데이털르 효율적으로 가공/처리할 수 있는 다양하고 훌륭한 기능제공.
- 판다스의 주요 구성 요소 - DataFrame, Series, Index



```python
import pandas as pd
```

**read_csv()**  
read_csv()를 이용하여 csv 파일을 편리하게 DataFrame으로 로딩  


```python
titanic_df = pd.read_csv('./pymldg-rev-master/1장/titanic_train.csv')
print('titanic 변수 type : ', type(titanic_df))
```

    titanic 변수 type :  <class 'pandas.core.frame.DataFrame'>
    

**head()**  
DataFrame의 맨 앞 일부 데이터만 추출.


```python
titanic_df.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>



**DataFrame의 생성**


```python
dic1 = {'Name' : ['chul','park','choi','kim'],
        'year' : [2011,2012,2013,2014],
        'Gender':['M','F','M','M']
       }

#딕셔너리를 DataFrame로변환
data_df = pd.DataFrame(dic1)
print(data_df)
print('#'*30)

# 새로운 컬럼명을 추가
data_df=pd.DataFrame(dic1, columns=['Name','year','Gender','age'])
print(data_df)
print('#'*30)

# 인덱스를 새로운 값으로 할당
data_df = pd.DataFrame(dic1, index = ['one','two','three','four'])
print(data_df)
print('#'*30)
```

       Name  year Gender
    0  chul  2011      M
    1  park  2012      F
    2  choi  2013      M
    3   kim  2014      M
    ##############################
       Name  year Gender  age
    0  chul  2011      M  NaN
    1  park  2012      F  NaN
    2  choi  2013      M  NaN
    3   kim  2014      M  NaN
    ##############################
           Name  year Gender
    one    chul  2011      M
    two    park  2012      F
    three  choi  2013      M
    four    kim  2014      M
    ##############################
    

**DataFrame의 컬렴명과 인덱스**


```python
print('columns:' ,titanic_df.columns)
print('iudex:' ,titanic_df.index)
print('value:', titanic_df.values)
```

    columns: Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
           'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
          dtype='object')
    iudex: RangeIndex(start=0, stop=891, step=1)
    value: [[1 0 3 ... 7.25 nan 'S']
     [2 1 1 ... 71.2833 'C85' 'C']
     [3 1 3 ... 7.925 nan 'S']
     ...
     [889 0 3 ... 23.45 nan 'S']
     [890 1 1 ... 30.0 'C148' 'C']
     [891 0 3 ... 7.75 nan 'Q']]
    

**DataFrame에서 Series 추출 및 DataFrame 필터링 추출**


```python
# DataFrame객체에서 [] 연산자 내에 한개의 칼럼만 입력하면 Series 객체를 반환
series  = titanic_df['Name']
print(series.head(3))
print('## type :',type(series))
print('')

# DataFrame객체에서 [] 연산자 내에  여러개의 칼럼을 입력하면 DataFrame 객체를 반환
df  = titanic_df[['Name','Age']]
print(df.head(3))
print('## type :',type(df))
print('')

# DataFrame객체에서 [] 연산자 내에 한개의 칼럼을 리스트로 입력하면 DataFrame 객체를 반환
one_col_df  = titanic_df[['Name']]
print(one_col_df.head(3))
print('## type :',type(one_col_df))
```

    0                              Braund, Mr. Owen Harris
    1    Cumings, Mrs. John Bradley (Florence Briggs Th...
    2                               Heikkinen, Miss. Laina
    Name: Name, dtype: object
    ## type : <class 'pandas.core.series.Series'>
    
                                                    Name   Age
    0                            Braund, Mr. Owen Harris  22.0
    1  Cumings, Mrs. John Bradley (Florence Briggs Th...  38.0
    2                             Heikkinen, Miss. Laina  26.0
    ## type : <class 'pandas.core.frame.DataFrame'>
    
                                                    Name
    0                            Braund, Mr. Owen Harris
    1  Cumings, Mrs. John Bradley (Florence Briggs Th...
    2                             Heikkinen, Miss. Laina
    ## type : <class 'pandas.core.frame.DataFrame'>
    

#### **shape** 
DataFrame의 행(row)와 열(Column 크기를 가지고 있는 속성이다.


```python
print('Dataframe 크기: ' , titanic_df.shape)
```

    Dataframe 크기:  (891, 12)
    

#### **info()**  
DataFrame내의 컬렴명, 데이터 타입,Null건수, 데이터 건수정보를  제공


```python
titanic_df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 891 entries, 0 to 890
    Data columns (total 12 columns):
     #   Column       Non-Null Count  Dtype  
    ---  ------       --------------  -----  
     0   PassengerId  891 non-null    int64  
     1   Survived     891 non-null    int64  
     2   Pclass       891 non-null    int64  
     3   Name         891 non-null    object 
     4   Sex          891 non-null    object 
     5   Age          714 non-null    float64
     6   SibSp        891 non-null    int64  
     7   Parch        891 non-null    int64  
     8   Ticket       891 non-null    object 
     9   Fare         891 non-null    float64
     10  Cabin        204 non-null    object 
     11  Embarked     889 non-null    object 
    dtypes: float64(2), int64(5), object(5)
    memory usage: 83.7+ KB
    

#### **describe()**  
데이터값들의 평균, 표준편차, 4분위 분포도를 제공합니다. 숫자형 컬럼들에 대해서 해당 정보를 제공


```python
titanic_df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Fare</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>891.000000</td>
      <td>891.000000</td>
      <td>891.000000</td>
      <td>714.000000</td>
      <td>891.000000</td>
      <td>891.000000</td>
      <td>891.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>446.000000</td>
      <td>0.383838</td>
      <td>2.308642</td>
      <td>29.699118</td>
      <td>0.523008</td>
      <td>0.381594</td>
      <td>32.204208</td>
    </tr>
    <tr>
      <th>std</th>
      <td>257.353842</td>
      <td>0.486592</td>
      <td>0.836071</td>
      <td>14.526497</td>
      <td>1.102743</td>
      <td>0.806057</td>
      <td>49.693429</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.420000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>223.500000</td>
      <td>0.000000</td>
      <td>2.000000</td>
      <td>20.125000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>7.910400</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>446.000000</td>
      <td>0.000000</td>
      <td>3.000000</td>
      <td>28.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>14.454200</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>668.500000</td>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>38.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>31.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>891.000000</td>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>80.000000</td>
      <td>8.000000</td>
      <td>6.000000</td>
      <td>512.329200</td>
    </tr>
  </tbody>
</table>
</div>



#### **value_counts()**    
` `  

동일한 개별 데이터 값이 몇건이 있는지 정보를 제공한다.   
즉 개별 데이터 값의 분포도를 제공한다 .  
주의할 점은 value_counts()는 Series 객체에서만 호출될 수 잇으므로 반드시 DataFrame를 단일 컬럼으로 입력하여 Series로 변환한 뒤 호출.


```python
value_counts = titanic_df['Pclass'].value_counts()
print(value_counts)
```

    3    491
    1    216
    2    184
    Name: Pclass, dtype: int64
    

#### **sort_values()** by=정렬컬럼, ascending=True 또는 False 로 오름차순/내림차순 정렬


```python
titanic_df.sort_values(by= 'Pclass',ascending=False)

titanic_df[['Name','Age']].sort_values(by='Age')
titanic_df[['Name','Age','Pclass']].sort_values(by=['Pclass','Age'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Age</th>
      <th>Pclass</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>305</th>
      <td>Allison, Master. Hudson Trevor</td>
      <td>0.92</td>
      <td>1</td>
    </tr>
    <tr>
      <th>297</th>
      <td>Allison, Miss. Helen Loraine</td>
      <td>2.00</td>
      <td>1</td>
    </tr>
    <tr>
      <th>445</th>
      <td>Dodge, Master. Washington</td>
      <td>4.00</td>
      <td>1</td>
    </tr>
    <tr>
      <th>802</th>
      <td>Carter, Master. William Thornton II</td>
      <td>11.00</td>
      <td>1</td>
    </tr>
    <tr>
      <th>435</th>
      <td>Carter, Miss. Lucile Polk</td>
      <td>14.00</td>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>859</th>
      <td>Razi, Mr. Raihed</td>
      <td>NaN</td>
      <td>3</td>
    </tr>
    <tr>
      <th>863</th>
      <td>Sage, Miss. Dorothy Edith "Dolly"</td>
      <td>NaN</td>
      <td>3</td>
    </tr>
    <tr>
      <th>868</th>
      <td>van Melkebeke, Mr. Philemon</td>
      <td>NaN</td>
      <td>3</td>
    </tr>
    <tr>
      <th>878</th>
      <td>Laleff, Mr. Kristo</td>
      <td>NaN</td>
      <td>3</td>
    </tr>
    <tr>
      <th>888</th>
      <td>Johnston, Miss. Catherine Helen "Carrie"</td>
      <td>NaN</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 3 columns</p>
</div>



# DataFramr과 리스트, 딕셔너리, 넘파이 ndarray 상호 변환
---
![image.png](attachment:image.png)

#### **리스트,ndarray에서 DataFrame변환**


```python
import numpy as np

col_name1 = ['col1']
list1= [1,2,3]
array1  = np.array(list1)

print('array1 shape:',array1.shape)
df_list1= pd.DataFrame(list1, columns= col_name1)
print('1차원 리스트로 만든 DataFrame:\n',df_list1)
df_array1 = pd.DataFrame(array1,columns = col_name1)
print('1차원 ndarray 만든 DataFrame:\n',df_array1)
```

    array1 shape: (3,)
    1차원 리스트로 만든 DataFrame:
        col1
    0     1
    1     2
    2     3
    1차원 ndarray 만든 DataFrame:
        col1
    0     1
    1     2
    2     3
    


```python
# 3개의 컬럼명이 필요함. 
col_name2=['col1', 'col2', 'col3']

# 2행x3열 형태의 리스트와 ndarray 생성 한 뒤 이를 DataFrame으로 변환. 
list2 = [[1, 2, 3],
         [11, 12, 13]]

array2 = np.array(list2)
print('array2 shape:', array2.shape )

df_list2 = pd.DataFrame(list2, columns=col_name2)
print('2차원 리스트로 만든 DataFrame:\n', df_list2)

df_array2 = pd.DataFrame(array2, columns=col_name2)
print('2차원 ndarray로 만든 DataFrame:\n', df_array2)
```

    array2 shape: (2, 3)
    2차원 리스트로 만든 DataFrame:
        col1  col2  col3
    0     1     2     3
    1    11    12    13
    2차원 ndarray로 만든 DataFrame:
        col1  col2  col3
    0     1     2     3
    1    11    12    13
    

#### **딕셔너리(dict)에서 DataFrame 변환**


```python
# Key는 컬럼명으로 매핑, Value는 리스트 형(또는 ndarray)
dic = {'col1':[1, 11], 'col2':[2, 22], 'col3':[3, 33]}
df_dict = pd.DataFrame(dic)
print('딕셔너리로 만든 DataFrame:\n', df_dict)
```

    딕셔너리로 만든 DataFrame:
        col1  col2  col3
    0     1     2     3
    1    11    22    33
    

#### **DataFrmae를 ndarray로 변환**


```python
# DataFrame을 ndarray로 변환
array3 = df_dict.values
print('df_dict.values 타입:', type(array3), 'df_dict.values shape:', array3.shape)
print(array3)
```

    df_dict.values 타입: <class 'numpy.ndarray'> df_dict.values shape: (2, 3)
    [[ 1  2  3]
     [11 22 33]]
    


```python
# DataFrame을 리스트로 변환
list3 = df_dict.values.tolist()
print('df_dict.values.tolist() 타입:', type(list3))
print(list3)

# DataFrame을 딕셔너리로 변환
dict3 = df_dict.to_dict('list')
print('\n df_dict.to_dict() 타입:', type(dict3))
print(dict3)
```

    df_dict.values.tolist() 타입: <class 'list'>
    [[1, 2, 3], [11, 22, 33]]
    
     df_dict.to_dict() 타입: <class 'dict'>
    {'col1': [1, 11], 'col2': [2, 22], 'col3': [3, 33]}
    

#### **DataFrame의 컬럼 데이터 셋 Access**  
DataFrame의 컬럼데이터 셋 생성과 수정은 [] 연산자를 이용해 쉽게 할 수 있다.


```python
titanic_df['age_0'] = 0
titanic_df.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>age_0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic_df['Age_by_10'] = titanic_df['Age']*10
titanic_df['Family_No'] = titanic_df['SibSp'] + titanic_df['Parch']+1
titanic_df.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>age_0</th>
      <th>Age_by_10</th>
      <th>Family_No</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
      <td>0</td>
      <td>220.0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
      <td>0</td>
      <td>380.0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
      <td>0</td>
      <td>260.0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



기존 컬럼에 값을 업데이트 하려면 해당 컬럼에 업데이트  값을 그대로 지정하면 됩니다.


```python
titanic_df['Age_by_10'] = titanic_df['Age_by_10']+100
titanic_df.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>age_0</th>
      <th>Age_by_10</th>
      <th>Family_No</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
      <td>0</td>
      <td>320.0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
      <td>0</td>
      <td>480.0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
      <td>0</td>
      <td>360.0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



#  DataFrame 데이터삭제
---
- DataFrame의 drop()  
`주요파라미터`  
- axis  : DataFrame의 로우를 삭제할 때는 axis = 0, 컬럼을 삭제할 때는 axis=1로 설정


```python
titanic_drop_df =  titanic_df.drop('age_0',axis=1)
titanic_drop_df.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>Age_by_10</th>
      <th>Family_No</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
      <td>320.0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
      <td>480.0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
      <td>360.0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



여러개의 컬럼들의 삭제는 drop의 인자로 삭제 컬럼들을 리스트로 입력.


```python
drop_result = titanic_df.drop(['age_0','Age_by_10','Family_No'],axis = 1,inplace=True)
print('inplace=True로 drop 후 반환된 값:', drop_result)
titanic_df.head(3)
```

    inplace=True로 drop 후 반환된 값: None
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>



axis = 0 일경우 drop()은 row 방향으로 데이터를 삭제합니다.


```python
print('### before axis 0 drop###')
print(titanic_df.head(5))
      
titanic_df.drop([0,1,2],axis =0,inplace=True)

print('### after axis 0 drop###')
titanic_df.head(3)
```

    ### before axis 0 drop###
       PassengerId  Survived  Pclass  \
    0            1         0       3   
    1            2         1       1   
    2            3         1       3   
    3            4         1       1   
    4            5         0       3   
    
                                                    Name     Sex   Age  SibSp  \
    0                            Braund, Mr. Owen Harris    male  22.0      1   
    1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   
    2                             Heikkinen, Miss. Laina  female  26.0      0   
    3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   
    4                           Allen, Mr. William Henry    male  35.0      0   
    
       Parch            Ticket     Fare Cabin Embarked  
    0      0         A/5 21171   7.2500   NaN        S  
    1      0          PC 17599  71.2833   C85        C  
    2      0  STON/O2. 3101282   7.9250   NaN        S  
    3      0            113803  53.1000  C123        S  
    4      0            373450   8.0500   NaN        S  
    ### after axis 0 drop###
       PassengerId  Survived  Pclass  \
    3            4         1       1   
    4            5         0       3   
    5            6         0       3   
    
                                               Name     Sex   Age  SibSp  Parch  \
    3  Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0   
    4                      Allen, Mr. William Henry    male  35.0      0      0   
    5                              Moran, Mr. James    male   NaN      0      0   
    
       Ticket     Fare Cabin Embarked  
    3  113803  53.1000  C123        S  
    4  373450   8.0500   NaN        S  
    5  330877   8.4583   NaN        Q  
    

**Index객체**


```python
# 원본 파일 재 로딩
titanic_df = pd.read_csv('./pymldg-rev-master/1장/titanic_train.csv')
# index 객체 추출
indexes = titanic_df.index
print(indexs)
# Index 객체를 실제 값 arrray로 변환 
print('Index 객체 array값:\n',indexes.values)
```

    RangeIndex(start=0, stop=891, step=1)
    Index 객체 array값:
     [  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17
      18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35
      36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53
      54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71
      72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89
      90  91  92  93  94  95  96  97  98  99 100 101 102 103 104 105 106 107
     108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125
     126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143
     144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161
     162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179
     180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197
     198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215
     216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233
     234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251
     252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269
     270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287
     288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305
     306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323
     324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341
     342 343 344 345 346 347 348 349 350 351 352 353 354 355 356 357 358 359
     360 361 362 363 364 365 366 367 368 369 370 371 372 373 374 375 376 377
     378 379 380 381 382 383 384 385 386 387 388 389 390 391 392 393 394 395
     396 397 398 399 400 401 402 403 404 405 406 407 408 409 410 411 412 413
     414 415 416 417 418 419 420 421 422 423 424 425 426 427 428 429 430 431
     432 433 434 435 436 437 438 439 440 441 442 443 444 445 446 447 448 449
     450 451 452 453 454 455 456 457 458 459 460 461 462 463 464 465 466 467
     468 469 470 471 472 473 474 475 476 477 478 479 480 481 482 483 484 485
     486 487 488 489 490 491 492 493 494 495 496 497 498 499 500 501 502 503
     504 505 506 507 508 509 510 511 512 513 514 515 516 517 518 519 520 521
     522 523 524 525 526 527 528 529 530 531 532 533 534 535 536 537 538 539
     540 541 542 543 544 545 546 547 548 549 550 551 552 553 554 555 556 557
     558 559 560 561 562 563 564 565 566 567 568 569 570 571 572 573 574 575
     576 577 578 579 580 581 582 583 584 585 586 587 588 589 590 591 592 593
     594 595 596 597 598 599 600 601 602 603 604 605 606 607 608 609 610 611
     612 613 614 615 616 617 618 619 620 621 622 623 624 625 626 627 628 629
     630 631 632 633 634 635 636 637 638 639 640 641 642 643 644 645 646 647
     648 649 650 651 652 653 654 655 656 657 658 659 660 661 662 663 664 665
     666 667 668 669 670 671 672 673 674 675 676 677 678 679 680 681 682 683
     684 685 686 687 688 689 690 691 692 693 694 695 696 697 698 699 700 701
     702 703 704 705 706 707 708 709 710 711 712 713 714 715 716 717 718 719
     720 721 722 723 724 725 726 727 728 729 730 731 732 733 734 735 736 737
     738 739 740 741 742 743 744 745 746 747 748 749 750 751 752 753 754 755
     756 757 758 759 760 761 762 763 764 765 766 767 768 769 770 771 772 773
     774 775 776 777 778 779 780 781 782 783 784 785 786 787 788 789 790 791
     792 793 794 795 796 797 798 799 800 801 802 803 804 805 806 807 808 809
     810 811 812 813 814 815 816 817 818 819 820 821 822 823 824 825 826 827
     828 829 830 831 832 833 834 835 836 837 838 839 840 841 842 843 844 845
     846 847 848 849 850 851 852 853 854 855 856 857 858 859 860 861 862 863
     864 865 866 867 868 869 870 871 872 873 874 875 876 877 878 879 880 881
     882 883 884 885 886 887 888 889 890]
    


```python
print(type(indexes.values))
print(indexes.values.shape)
print(indexes[:5].values)
print(indexes.values[:5])
print(indexes[6])
```

    <class 'numpy.ndarray'>
    (891,)
    [0 1 2 3 4]
    [0 1 2 3 4]
    6
    


```python
indexes[0] = 5
```

Series 객체는 Index 객체를 포함하지만 Series 객체에 영산 함수를 적용할 때 
Index 는 연산에서 제외된다. Index 는 오직 식별용이다.


```python
series_fair = titanic_df['Fare']
series_fair.head(5)
```




    0     7.2500
    1    71.2833
    2     7.9250
    3    53.1000
    4     8.0500
    Name: Fare, dtype: float64




```python
series_fair = titanic_df['Fare']
print('Fair Series max 값:', series_fair.max())
print('Fair Series sum 값:', series_fair.sum())
print('sum() Fair Series:', sum(series_fair))
print('Fair Series + 3:\n',(series_fair + 3).head(3) )
```

    Fair Series max 값: 512.3292
    Fair Series sum 값: 28693.9493
    sum() Fair Series: 28693.949299999967
    Fair Series + 3:
     0    10.2500
    1    74.2833
    2    10.9250
    Name: Fare, dtype: float64
    

DataFrame 및 Series에 reset_index() 메서드를 수행하면 새롭게 인덱스를 연속 숫자형으로 할당하며 기존 인덱스는 'index'라는 새로운 컬렴명으로 추가된다.


```python
titanic_reset_df = titanic_df.reset_index(inplace=False)
titanic_reset_df.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
print('### before reset_index ###')
value_counts = titanic_df['Pclass'].value_counts()
print(value_counts)
print('value_counts 객체 변수 타입:',type(value_counts))

new_value_counts = value_counts.reset_index(inplace=False)
print('### After reset_index ###')
print(new_value_counts)
print('new_value_counts 객체 변수 타입:',type(new_value_counts))
```

# 데이터 셀렉션 및 필터링
---
- DataFrame의 [] 연산자


```python
print('단일 컬럼 데이터 추출:\n', titanic_df[ 'Pclass' ].head(3))
print('\n여러 컬럼들의 데이터 추출:\n', titanic_df[ ['Survived', 'Pclass'] ].head(3))
print('[ ] 안에 숫자 index는 KeyError 오류 발생:\n', titanic_df[0])
```

    단일 컬럼 데이터 추출:
     0    3
    1    1
    2    3
    Name: Pclass, dtype: int64
    
    여러 컬럼들의 데이터 추출:
        Survived  Pclass
    0         0       3
    1         1       1
    2         1       3
    


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    C:\anaconda3\lib\site-packages\pandas\core\indexes\base.py in get_loc(self, key, method, tolerance)
       2890             try:
    -> 2891                 return self._engine.get_loc(casted_key)
       2892             except KeyError as err:
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    KeyError: 0

    
    The above exception was the direct cause of the following exception:
    

    KeyError                                  Traceback (most recent call last)

    <ipython-input-73-db364dee1383> in <module>
          1 print('단일 컬럼 데이터 추출:\n', titanic_df[ 'Pclass' ].head(3))
          2 print('\n여러 컬럼들의 데이터 추출:\n', titanic_df[ ['Survived', 'Pclass'] ].head(3))
    ----> 3 print('[ ] 안에 숫자 index는 KeyError 오류 발생:\n', titanic_df[0])
    

    C:\anaconda3\lib\site-packages\pandas\core\frame.py in __getitem__(self, key)
       2900             if self.columns.nlevels > 1:
       2901                 return self._getitem_multilevel(key)
    -> 2902             indexer = self.columns.get_loc(key)
       2903             if is_integer(indexer):
       2904                 indexer = [indexer]
    

    C:\anaconda3\lib\site-packages\pandas\core\indexes\base.py in get_loc(self, key, method, tolerance)
       2891                 return self._engine.get_loc(casted_key)
       2892             except KeyError as err:
    -> 2893                 raise KeyError(key) from err
       2894 
       2895         if tolerance is not None:
    

    KeyError: 0



```python
titanic_df[0:2]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic_df[titanic_df['Pclass']==3].head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.925</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.050</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
data = {'Name': ['Chulmin', 'Eunkyung','Jinwoong','Soobeom'],
        'Year': [2011, 2016, 2015, 2015],
        'Gender': ['Male', 'Female', 'Male', 'Male']
       }
data = pd.DataFrame(data,index = ['one','two','three','four'])
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Year</th>
      <th>Gender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>one</th>
      <td>Chulmin</td>
      <td>2011</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>two</th>
      <td>Eunkyung</td>
      <td>2016</td>
      <td>Female</td>
    </tr>
    <tr>
      <th>three</th>
      <td>Jinwoong</td>
      <td>2015</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>four</th>
      <td>Soobeom</td>
      <td>2015</td>
      <td>Male</td>
    </tr>
  </tbody>
</table>
</div>



- 명칭 기반 인덱싱과 위치 기반 인덱싱의 구분


```python
# data_df 를 reset_index() 로 새로운 숫자형 인덱스를 생성
data_df_reset = data_df.reset_index()
data_df_reset = data_df_reset.rename(columns={'index':'old_index'})

# index 값에 1을 더해서 1부터 시작하는 새로운 index값 생성
data_df_reset.index = data_df_reset.index+1
data_df_reset
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>old_index</th>
      <th>Name</th>
      <th>year</th>
      <th>Gender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>one</td>
      <td>chul</td>
      <td>2011</td>
      <td>M</td>
    </tr>
    <tr>
      <th>2</th>
      <td>two</td>
      <td>park</td>
      <td>2012</td>
      <td>F</td>
    </tr>
    <tr>
      <th>3</th>
      <td>three</td>
      <td>choi</td>
      <td>2013</td>
      <td>M</td>
    </tr>
    <tr>
      <th>4</th>
      <td>four</td>
      <td>kim</td>
      <td>2014</td>
      <td>M</td>
    </tr>
  </tbody>
</table>
</div>



- DataFrame iloc[] 연산자


```python
data_df_reset.iloc[0, 1]
```




    'chul'



- DataFrame loc[] 연산자


```python
data_df.loc['one', 'Name']
```




    'chul'




```python
print(data_df_reset.loc[1:2 , 'Name'])
```

    1    chul
    2    park
    Name: Name, dtype: object
    

- 불린 인덱싱


```python
titanic_df = pd.read_csv('./pymldg-rev-master/1장/titanic_train.csv')
titanic_boolean = titanic_df[titanic_df['Age'] > 60]
print(type(titanic_boolean))
titanic_boolean
```

    <class 'pandas.core.frame.DataFrame'>
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>33</th>
      <td>34</td>
      <td>0</td>
      <td>2</td>
      <td>Wheadon, Mr. Edward H</td>
      <td>male</td>
      <td>66.0</td>
      <td>0</td>
      <td>0</td>
      <td>C.A. 24579</td>
      <td>10.5000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>54</th>
      <td>55</td>
      <td>0</td>
      <td>1</td>
      <td>Ostby, Mr. Engelhart Cornelius</td>
      <td>male</td>
      <td>65.0</td>
      <td>0</td>
      <td>1</td>
      <td>113509</td>
      <td>61.9792</td>
      <td>B30</td>
      <td>C</td>
    </tr>
    <tr>
      <th>96</th>
      <td>97</td>
      <td>0</td>
      <td>1</td>
      <td>Goldschmidt, Mr. George B</td>
      <td>male</td>
      <td>71.0</td>
      <td>0</td>
      <td>0</td>
      <td>PC 17754</td>
      <td>34.6542</td>
      <td>A5</td>
      <td>C</td>
    </tr>
    <tr>
      <th>116</th>
      <td>117</td>
      <td>0</td>
      <td>3</td>
      <td>Connors, Mr. Patrick</td>
      <td>male</td>
      <td>70.5</td>
      <td>0</td>
      <td>0</td>
      <td>370369</td>
      <td>7.7500</td>
      <td>NaN</td>
      <td>Q</td>
    </tr>
    <tr>
      <th>170</th>
      <td>171</td>
      <td>0</td>
      <td>1</td>
      <td>Van der hoef, Mr. Wyckoff</td>
      <td>male</td>
      <td>61.0</td>
      <td>0</td>
      <td>0</td>
      <td>111240</td>
      <td>33.5000</td>
      <td>B19</td>
      <td>S</td>
    </tr>
    <tr>
      <th>252</th>
      <td>253</td>
      <td>0</td>
      <td>1</td>
      <td>Stead, Mr. William Thomas</td>
      <td>male</td>
      <td>62.0</td>
      <td>0</td>
      <td>0</td>
      <td>113514</td>
      <td>26.5500</td>
      <td>C87</td>
      <td>S</td>
    </tr>
    <tr>
      <th>275</th>
      <td>276</td>
      <td>1</td>
      <td>1</td>
      <td>Andrews, Miss. Kornelia Theodosia</td>
      <td>female</td>
      <td>63.0</td>
      <td>1</td>
      <td>0</td>
      <td>13502</td>
      <td>77.9583</td>
      <td>D7</td>
      <td>S</td>
    </tr>
    <tr>
      <th>280</th>
      <td>281</td>
      <td>0</td>
      <td>3</td>
      <td>Duane, Mr. Frank</td>
      <td>male</td>
      <td>65.0</td>
      <td>0</td>
      <td>0</td>
      <td>336439</td>
      <td>7.7500</td>
      <td>NaN</td>
      <td>Q</td>
    </tr>
    <tr>
      <th>326</th>
      <td>327</td>
      <td>0</td>
      <td>3</td>
      <td>Nysveen, Mr. Johan Hansen</td>
      <td>male</td>
      <td>61.0</td>
      <td>0</td>
      <td>0</td>
      <td>345364</td>
      <td>6.2375</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>438</th>
      <td>439</td>
      <td>0</td>
      <td>1</td>
      <td>Fortune, Mr. Mark</td>
      <td>male</td>
      <td>64.0</td>
      <td>1</td>
      <td>4</td>
      <td>19950</td>
      <td>263.0000</td>
      <td>C23 C25 C27</td>
      <td>S</td>
    </tr>
    <tr>
      <th>456</th>
      <td>457</td>
      <td>0</td>
      <td>1</td>
      <td>Millet, Mr. Francis Davis</td>
      <td>male</td>
      <td>65.0</td>
      <td>0</td>
      <td>0</td>
      <td>13509</td>
      <td>26.5500</td>
      <td>E38</td>
      <td>S</td>
    </tr>
    <tr>
      <th>483</th>
      <td>484</td>
      <td>1</td>
      <td>3</td>
      <td>Turkula, Mrs. (Hedwig)</td>
      <td>female</td>
      <td>63.0</td>
      <td>0</td>
      <td>0</td>
      <td>4134</td>
      <td>9.5875</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>493</th>
      <td>494</td>
      <td>0</td>
      <td>1</td>
      <td>Artagaveytia, Mr. Ramon</td>
      <td>male</td>
      <td>71.0</td>
      <td>0</td>
      <td>0</td>
      <td>PC 17609</td>
      <td>49.5042</td>
      <td>NaN</td>
      <td>C</td>
    </tr>
    <tr>
      <th>545</th>
      <td>546</td>
      <td>0</td>
      <td>1</td>
      <td>Nicholson, Mr. Arthur Ernest</td>
      <td>male</td>
      <td>64.0</td>
      <td>0</td>
      <td>0</td>
      <td>693</td>
      <td>26.0000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>555</th>
      <td>556</td>
      <td>0</td>
      <td>1</td>
      <td>Wright, Mr. George</td>
      <td>male</td>
      <td>62.0</td>
      <td>0</td>
      <td>0</td>
      <td>113807</td>
      <td>26.5500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>570</th>
      <td>571</td>
      <td>1</td>
      <td>2</td>
      <td>Harris, Mr. George</td>
      <td>male</td>
      <td>62.0</td>
      <td>0</td>
      <td>0</td>
      <td>S.W./PP 752</td>
      <td>10.5000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>625</th>
      <td>626</td>
      <td>0</td>
      <td>1</td>
      <td>Sutton, Mr. Frederick</td>
      <td>male</td>
      <td>61.0</td>
      <td>0</td>
      <td>0</td>
      <td>36963</td>
      <td>32.3208</td>
      <td>D50</td>
      <td>S</td>
    </tr>
    <tr>
      <th>630</th>
      <td>631</td>
      <td>1</td>
      <td>1</td>
      <td>Barkworth, Mr. Algernon Henry Wilson</td>
      <td>male</td>
      <td>80.0</td>
      <td>0</td>
      <td>0</td>
      <td>27042</td>
      <td>30.0000</td>
      <td>A23</td>
      <td>S</td>
    </tr>
    <tr>
      <th>672</th>
      <td>673</td>
      <td>0</td>
      <td>2</td>
      <td>Mitchell, Mr. Henry Michael</td>
      <td>male</td>
      <td>70.0</td>
      <td>0</td>
      <td>0</td>
      <td>C.A. 24580</td>
      <td>10.5000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>745</th>
      <td>746</td>
      <td>0</td>
      <td>1</td>
      <td>Crosby, Capt. Edward Gifford</td>
      <td>male</td>
      <td>70.0</td>
      <td>1</td>
      <td>1</td>
      <td>WE/P 5735</td>
      <td>71.0000</td>
      <td>B22</td>
      <td>S</td>
    </tr>
    <tr>
      <th>829</th>
      <td>830</td>
      <td>1</td>
      <td>1</td>
      <td>Stone, Mrs. George Nelson (Martha Evelyn)</td>
      <td>female</td>
      <td>62.0</td>
      <td>0</td>
      <td>0</td>
      <td>113572</td>
      <td>80.0000</td>
      <td>B28</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>851</th>
      <td>852</td>
      <td>0</td>
      <td>3</td>
      <td>Svensson, Mr. Johan</td>
      <td>male</td>
      <td>74.0</td>
      <td>0</td>
      <td>0</td>
      <td>347060</td>
      <td>7.7750</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic_df[titanic_df['Age'] > 60][['Name','Age']].head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>33</th>
      <td>Wheadon, Mr. Edward H</td>
      <td>66.0</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Ostby, Mr. Engelhart Cornelius</td>
      <td>65.0</td>
    </tr>
    <tr>
      <th>96</th>
      <td>Goldschmidt, Mr. George B</td>
      <td>71.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic_df[['Name','Age']][titanic_df['Age'] > 60].head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>33</th>
      <td>Wheadon, Mr. Edward H</td>
      <td>66.0</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Ostby, Mr. Engelhart Cornelius</td>
      <td>65.0</td>
    </tr>
    <tr>
      <th>96</th>
      <td>Goldschmidt, Mr. George B</td>
      <td>71.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic_df.loc[titanic_df['Age']> 60, ['Name','Age']].head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>33</th>
      <td>Wheadon, Mr. Edward H</td>
      <td>66.0</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Ostby, Mr. Engelhart Cornelius</td>
      <td>65.0</td>
    </tr>
    <tr>
      <th>96</th>
      <td>Goldschmidt, Mr. George B</td>
      <td>71.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic_df[ (titanic_df['Age'] > 60) & (titanic_df['Pclass']==1) & (titanic_df['Sex']=='female')]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>275</th>
      <td>276</td>
      <td>1</td>
      <td>1</td>
      <td>Andrews, Miss. Kornelia Theodosia</td>
      <td>female</td>
      <td>63.0</td>
      <td>1</td>
      <td>0</td>
      <td>13502</td>
      <td>77.9583</td>
      <td>D7</td>
      <td>S</td>
    </tr>
    <tr>
      <th>829</th>
      <td>830</td>
      <td>1</td>
      <td>1</td>
      <td>Stone, Mrs. George Nelson (Martha Evelyn)</td>
      <td>female</td>
      <td>62.0</td>
      <td>0</td>
      <td>0</td>
      <td>113572</td>
      <td>80.0000</td>
      <td>B28</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



조건식은 변수로도 할당가능 합니다.복잡한 조건식은  변수로  할당하여  ㄱ ㅏ독성을 향상 할 수 있습니다.


```python
cond1 = titanic_df['Age'] > 60
cond2 = titanic_df['Pclass']==1
cond3 = titanic_df['Sex']=='female'
titanic_df[ cond1 & cond2 & cond3]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>275</th>
      <td>276</td>
      <td>1</td>
      <td>1</td>
      <td>Andrews, Miss. Kornelia Theodosia</td>
      <td>female</td>
      <td>63.0</td>
      <td>1</td>
      <td>0</td>
      <td>13502</td>
      <td>77.9583</td>
      <td>D7</td>
      <td>S</td>
    </tr>
    <tr>
      <th>829</th>
      <td>830</td>
      <td>1</td>
      <td>1</td>
      <td>Stone, Mrs. George Nelson (Martha Evelyn)</td>
      <td>female</td>
      <td>62.0</td>
      <td>0</td>
      <td>0</td>
      <td>113572</td>
      <td>80.0000</td>
      <td>B28</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



#  Aggregation 함수
---
- sum(),max(), min(),count() 등의 함수는 DataFrame/Series에서 집합 연산을 수행
- DataFrame의 경우 DataFrame에서 바로 aggregation을 호출할 경우 모든 컬럼에 해당 aggreegation 을 적용

- Aggregation 함수


```python
# NaN값은 count 에서 제외
titanic_df.count()
```




    PassengerId    891
    Survived       891
    Pclass         891
    Name           891
    Sex            891
    Age            714
    SibSp          891
    Parch          891
    Ticket         891
    Fare           891
    Cabin          204
    Embarked       889
    dtype: int64



특정 칼럼들로 Aggregation 함수 수행


```python
titanic_df[['Age','Fare']].mean()
```




    Age     29.699118
    Fare    32.204208
    dtype: float64




```python
titanic_df[['Age','Fare']].sum()
```




    Age     21205.1700
    Fare    28693.9493
    dtype: float64




```python
titanic_df[['Age','Fare']].count()
```

특정 컬럼들로 Aggregation 함수 수행.


```python
titanic_df[['Age','Fare']].mean(axis=1)
```




    0      14.62500
    1      54.64165
    2      16.96250
    3      44.05000
    4      21.52500
             ...   
    886    20.00000
    887    24.50000
    888    23.45000
    889    28.00000
    890    19.87500
    Length: 891, dtype: float64




```python
titanic_df[['Age', 'Fare']].mean()
```




    Age     29.699118
    Fare    32.204208
    dtype: float64



# DataFrame Group By
---
- DataFrame은 Group by 연산을 위해 groupby() 메서드 제공
- groupby()  메소드는 by 인자로 gropu by 하려는 컬럼명을 입력 받으면 DataFrameGroupBy 객체를 반환
- 이렇게 반환된 DataFrameGroup By 객체에 aggregation 함수를 수행

**groupby()** 인자에 Group By 하고자 하는 컬럼을 입력, 여러개의 컬럼으로 Group by 하고자 하면 [] 내에 해당 컬럼명을 입력. Dataframe에 groupby()를 호출하면 DataFramegroupvBy 객체를 반환


```python
titanic_groupby = titanic_df.groupby(by='Pclass')
print(type(titanic_groupby))
print(titanic_groupby)
```

    <class 'pandas.core.groupby.generic.DataFrameGroupBy'>
    <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000029CBCDE9988>
    

DataFrameGroupby객체에 Aggregation 함수를 호출하여 Group by 수행.


```python
titanic_groupby = titanic_df.groupby('Pclass').count()
titanic_groupby
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
    <tr>
      <th>Pclass</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>216</td>
      <td>216</td>
      <td>216</td>
      <td>216</td>
      <td>186</td>
      <td>216</td>
      <td>216</td>
      <td>216</td>
      <td>216</td>
      <td>176</td>
      <td>214</td>
    </tr>
    <tr>
      <th>2</th>
      <td>184</td>
      <td>184</td>
      <td>184</td>
      <td>184</td>
      <td>173</td>
      <td>184</td>
      <td>184</td>
      <td>184</td>
      <td>184</td>
      <td>16</td>
      <td>184</td>
    </tr>
    <tr>
      <th>3</th>
      <td>491</td>
      <td>491</td>
      <td>491</td>
      <td>491</td>
      <td>355</td>
      <td>491</td>
      <td>491</td>
      <td>491</td>
      <td>491</td>
      <td>12</td>
      <td>491</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic_groupby = titanic_df.groupby('Pclass')[['PassengerId', 'Survived']].count()
titanic_groupby
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
    </tr>
    <tr>
      <th>Pclass</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>216</td>
      <td>216</td>
    </tr>
    <tr>
      <th>2</th>
      <td>184</td>
      <td>184</td>
    </tr>
    <tr>
      <th>3</th>
      <td>491</td>
      <td>491</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic_df[['Pclass','PassengerId','Survived']].groupby('Pclass').count()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
    </tr>
    <tr>
      <th>Pclass</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>216</td>
      <td>216</td>
    </tr>
    <tr>
      <th>2</th>
      <td>184</td>
      <td>184</td>
    </tr>
    <tr>
      <th>3</th>
      <td>491</td>
      <td>491</td>
    </tr>
  </tbody>
</table>
</div>



RDBMS의 group by 는 select절에 여러개의 aggregationnn 함수를 적용할 수 있음.  
판다스는 여러개의 aggregation ㅎ마수를 적용할 수 있도록 agg() 함수를 별도로 제공


```python
titanic_df.groupby('Pclass')['Age'].agg([max,min])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>max</th>
      <th>min</th>
    </tr>
    <tr>
      <th>Pclass</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>80.0</td>
      <td>0.92</td>
    </tr>
    <tr>
      <th>2</th>
      <td>70.0</td>
      <td>0.67</td>
    </tr>
    <tr>
      <th>3</th>
      <td>74.0</td>
      <td>0.42</td>
    </tr>
  </tbody>
</table>
</div>



딕셔너리를 이용하여 다양한 aggregation 함수를 적용


```python
# 컬렴명 : 함수 순으로 넣음. 
agg_format={'Age':'max', 'SibSp':'sum', 'Fare':'mean'}
titanic_df.groupby('Pclass').agg(agg_format)
```

# 결측치 처리
---
- isna() : DataFrame의 isna() 메소드는 주어진 컬람값들이 NaN인지 True/False 값을 반환
- fillna() : Missing 데이터를 인자로 주어진 값으로 대체.


```python
titanic_df.isna().head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



아래와 같이 isna() 반환 결과에 sum()을 호출하여 컬럼별로 NaN 건수를 구할 수 있다.


```python
titanic_df.isna().sum()
```




    PassengerId      0
    Survived         0
    Pclass           0
    Name             0
    Sex              0
    Age            177
    SibSp            0
    Parch            0
    Ticket           0
    Fare             0
    Cabin          687
    Embarked         2
    dtype: int64



**fillna() 로 Missing 데이터 대체하기**


```python
titanic_df['Cabin'] = titanic_df['Cabin'].fillna('C000')
titanic_df.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>C000</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>C000</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic_df['Age'] = titanic_df['Age'].fillna(titanic_df['Age'].mean())
titanic_df['Embarked'] = titanic_df['Embarked'].fillna('S')
titanic_df.isna().sum()
```




    PassengerId    0
    Survived       0
    Pclass         0
    Name           0
    Sex            0
    Age            0
    SibSp          0
    Parch          0
    Ticket         0
    Fare           0
    Cabin          0
    Embarked       0
    dtype: int64



# apply lambda 식으로 데이터 가공
---
판다스는 apply 함수에 lambda 식을 결합해  DataFrame이나 Series의 레코드별로 데이터를 가공하는 기능을 제공. 판다스의 경우 컬럼에 일괄적으로 데이터 가공을 하는 것이 속도 면에서 더 빠르나 복잡한 데이터 각공은 어쩔 수 없이 apply lambda 를 이용
![image.png](attachment:image.png)

- 파이썬의 lambda식 기본



```python
def get_square(a):
    return a**2

print('3의 제곱은 : ',get_square(3))
```

    3의 제곱은 :  9
    


```python
a =[1,2,3]
squares = map(lambda x:  x**2,a)
list(squares)
```




    [1, 4, 9]



- 판다스에 apply lambda 식 적용


```python
titanic_df['Name_len'] = titanic_df['Name'].apply(lambda x : len(x))
titanic_df[['Name','Name_len']].head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Name_len</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Braund, Mr. Owen Harris</td>
      <td>23</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>51</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Heikkinen, Miss. Laina</td>
      <td>22</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic_df['Child_Adult'] = titanic_df['Age'].apply(lambda x :'Child' if x <=15 else 'Adult')
titanic_df[['Age','Child_Adult']].head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Child_Adult</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>22.000000</td>
      <td>Adult</td>
    </tr>
    <tr>
      <th>1</th>
      <td>38.000000</td>
      <td>Adult</td>
    </tr>
    <tr>
      <th>2</th>
      <td>26.000000</td>
      <td>Adult</td>
    </tr>
    <tr>
      <th>3</th>
      <td>35.000000</td>
      <td>Adult</td>
    </tr>
    <tr>
      <th>4</th>
      <td>35.000000</td>
      <td>Adult</td>
    </tr>
    <tr>
      <th>5</th>
      <td>29.699118</td>
      <td>Adult</td>
    </tr>
    <tr>
      <th>6</th>
      <td>54.000000</td>
      <td>Adult</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2.000000</td>
      <td>Child</td>
    </tr>
    <tr>
      <th>8</th>
      <td>27.000000</td>
      <td>Adult</td>
    </tr>
    <tr>
      <th>9</th>
      <td>14.000000</td>
      <td>Child</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic_df['Age_cat'] = titanic_df['Age'].apply(lambda x :'Child' if x <=15 else 
                                                    ('Adult' if x <=60 else 'Elderly'))
titanic_df['Age_cat'].value_counts()
```




    Adult      786
    Child       83
    Elderly     22
    Name: Age_cat, dtype: int64




```python
# 나이에 따라 세분화된 분류를 수행하는 함수 생성. 
def get_category(age):
    cat = ''
    if age <= 5: cat = 'Baby'
    elif age <= 12: cat = 'Child'
    elif age <= 18: cat = 'Teenager'
    elif age <= 25: cat = 'Student'
    elif age <= 35: cat = 'Young Adult'
    elif age <= 60: cat = 'Adult'
    else : cat = 'Elderly'
    
    return cat

# lambda 식에 위에서 생성한 get_category( ) 함수를 반환값으로 지정. 
# get_category(X)는 입력값으로 ‘Age’ 컬럼 값을 받아서 해당하는 cat 반환
titanic_df['Age_cat'] = titanic_df['Age'].apply(lambda x : get_category(x))
titanic_df[['Age','Age_cat']].head()
    
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Age_cat</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>22.0</td>
      <td>Student</td>
    </tr>
    <tr>
      <th>1</th>
      <td>38.0</td>
      <td>Adult</td>
    </tr>
    <tr>
      <th>2</th>
      <td>26.0</td>
      <td>Young Adult</td>
    </tr>
    <tr>
      <th>3</th>
      <td>35.0</td>
      <td>Young Adult</td>
    </tr>
    <tr>
      <th>4</th>
      <td>35.0</td>
      <td>Young Adult</td>
    </tr>
  </tbody>
</table>
</div>


