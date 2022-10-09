# Pandas
---
> 파이썬의 데이터 구조 셋은 이미 잘갖추어져 있지만, pandas 모듈은 여기에 두가지 컨테이너인 Series와 DataFrame을 추가한다.
- 시리즈는 레이블이 붙은 1차원 벡터다.
- 프레임은 레이블이 붙은 행과 열로 구성된 테이블이다.
- 프레임의 각 열은 시리즈다. 몇 가지 예외를 제외하면 pandas는 프레임을 시리즈와 유사하게 취급한다
- 프레임과 시리즈는 다음과 같이 다양한 데이터 전처리함수를 가진다.
        - 단순 혹은계층적 인덱싱
        - 결측치 처리
        - 전체 열과 테이블에서 사칙 ,논리 연산
        - 데이터 베이스 - 타입연산 (결합이나 집계 등)
        - 단일 열이나 전체 테이블 시각화
        - 파일에서 데이터 읽고 쓰기


## 시리즈 : 1차원 벡터
---


```python
import pandas as pd

series = pd.Series((2,3,2,6,4,1,2,3,45,1,2,3,4,2,-1,-2,))
print(len(series))
print(series)
```

    16
    0      2
    1      3
    2      2
    3      6
    4      4
    5      1
    6      2
    7      3
    8     45
    9      1
    10     2
    11     3
    12     4
    13     2
    14    -1
    15    -2
    dtype: int64
    

## 시리즈의 인덱스는 정수형이 기본값이다.
---


```python
series.index.values
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15],
          dtype=int64)



## 프레임 
---
>레이블이 붙은 행과 열로 구성된 테이블
- 데이터 프레임은 2차원 numpy 배열, 튜플로 구성된 리스트,파이썬 딕셔너리  
  와 또 다른 데이터 프레임으로 생성 가능


```python
import pandas as pd
alco2009 = pd.read_csv('./2020-08/excel/niaaa-report2009.csv',index_col="State")
alco2009.head()
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
      <th>Beer</th>
      <th>Wine</th>
      <th>Spirits</th>
    </tr>
    <tr>
      <th>State</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama</th>
      <td>1.20</td>
      <td>0.22</td>
      <td>0.58</td>
    </tr>
    <tr>
      <th>Alaska</th>
      <td>1.31</td>
      <td>0.54</td>
      <td>1.16</td>
    </tr>
    <tr>
      <th>Arizona</th>
      <td>1.19</td>
      <td>0.38</td>
      <td>0.74</td>
    </tr>
    <tr>
      <th>Arkansas</th>
      <td>1.07</td>
      <td>0.17</td>
      <td>0.60</td>
    </tr>
    <tr>
      <th>California</th>
      <td>1.05</td>
      <td>0.55</td>
      <td>0.73</td>
    </tr>
  </tbody>
</table>
</div>



## 데이터 모양 바꾸기
---

- reset_index()와 set_index(column) 함수는 기존 인덱스를 떼어 내거나 새로운 인덱스를 만든다  
- 옵셔널 파라미터 inplace = True가 주어미녀 기존 데이터 프레임 자체를 수정한다


```python
alco2009.reset_index().head()
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
      <th>State</th>
      <th>Beer</th>
      <th>Wine</th>
      <th>Spirits</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alabama</td>
      <td>1.20</td>
      <td>0.22</td>
      <td>0.58</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alaska</td>
      <td>1.31</td>
      <td>0.54</td>
      <td>1.16</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Arizona</td>
      <td>1.19</td>
      <td>0.38</td>
      <td>0.74</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Arkansas</td>
      <td>1.07</td>
      <td>0.17</td>
      <td>0.60</td>
    </tr>
    <tr>
      <th>4</th>
      <td>California</td>
      <td>1.05</td>
      <td>0.55</td>
      <td>0.73</td>
    </tr>
  </tbody>
</table>
</div>




```python
alco2009.reset_index().set_index("Beer").head()
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
      <th>State</th>
      <th>Wine</th>
      <th>Spirits</th>
    </tr>
    <tr>
      <th>Beer</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1.20</th>
      <td>Alabama</td>
      <td>0.22</td>
      <td>0.58</td>
    </tr>
    <tr>
      <th>1.31</th>
      <td>Alaska</td>
      <td>0.54</td>
      <td>1.16</td>
    </tr>
    <tr>
      <th>1.19</th>
      <td>Arizona</td>
      <td>0.38</td>
      <td>0.74</td>
    </tr>
    <tr>
      <th>1.07</th>
      <td>Arkansas</td>
      <td>0.17</td>
      <td>0.60</td>
    </tr>
    <tr>
      <th>1.05</th>
      <td>California</td>
      <td>0.55</td>
      <td>0.73</td>
    </tr>
  </tbody>
</table>
</div>



## 재인덱싱 
> 기존 데이터 프레임과 시리즈에서 행이나 열,행과 열을 추려서 새 데이터 프레임이나 시리즈를 생성한다


```python
s_states = [state for state in alco2009.index if state[0]=='S']+["Samoa"]
print(s_states)

drinks = list(alco2009.columns)+['Water']
print(drinks)
nan_alco = alco2009.reindex(s_states, columns = drinks)
nan_alco
```

    ['South Carolina', 'South Dakota', 'Samoa']
    ['Beer', 'Wine', 'Spirits', 'Water']
    




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
      <th>Beer</th>
      <th>Wine</th>
      <th>Spirits</th>
      <th>Water</th>
    </tr>
    <tr>
      <th>State</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>South Carolina</th>
      <td>1.36</td>
      <td>0.24</td>
      <td>0.77</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>South Dakota</th>
      <td>1.53</td>
      <td>0.22</td>
      <td>0.88</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Samoa</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## 스태킹과 피보팅
---
> 열 이름을 계층화 하는 대신 멀티인덱스의 전체 혹은 일부를 평평하게 할 수도 있다.
반대로 인덱스를 계층화 하는 대신 다층으로 구성된 열이름의 전체나 일부를 평평하게 할 수도 있다. 

- stack() 함수는 인덱스의 레벨 개수를 증가시키는 동시에 열 이름의 레벨 개수를 감소 시킨다**
- unstack() 함수는 인덱스 레벨 개수를 낮추고 열 이름의 레벨 개수를 높인다.
- pivot(index,columns,values) 함수는 기존 데이터 프레임을 새로운 데이터 프레임으로 변환.  

 **그 과정에서 index로 넘기는열을 새로운 인덱스로 사용하고 ,columns를 새로운 열 이름 리스로 사용하며 values 에 해당하는 열은 데이터 프레임을 채우는 데이터로 사용한다.**


```python
alco = pd.read_csv("./2020-08/excel/niaaa-report.csv",index_col=["State","Year"])
alco
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
      <th></th>
      <th>Beer</th>
      <th>Wine</th>
      <th>Spirits</th>
    </tr>
    <tr>
      <th>State</th>
      <th>Year</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">Alabama</th>
      <th>1977</th>
      <td>0.99</td>
      <td>0.13</td>
      <td>0.84</td>
    </tr>
    <tr>
      <th>1978</th>
      <td>0.98</td>
      <td>0.12</td>
      <td>0.88</td>
    </tr>
    <tr>
      <th>1979</th>
      <td>0.98</td>
      <td>0.12</td>
      <td>0.84</td>
    </tr>
    <tr>
      <th>1980</th>
      <td>0.96</td>
      <td>0.16</td>
      <td>0.74</td>
    </tr>
    <tr>
      <th>1981</th>
      <td>1.00</td>
      <td>0.19</td>
      <td>0.73</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">Wyoming</th>
      <th>2005</th>
      <td>1.21</td>
      <td>0.23</td>
      <td>0.97</td>
    </tr>
    <tr>
      <th>2006</th>
      <td>1.47</td>
      <td>0.23</td>
      <td>1.05</td>
    </tr>
    <tr>
      <th>2007</th>
      <td>1.49</td>
      <td>0.23</td>
      <td>1.10</td>
    </tr>
    <tr>
      <th>2008</th>
      <td>1.54</td>
      <td>0.23</td>
      <td>1.12</td>
    </tr>
    <tr>
      <th>2009</th>
      <td>1.45</td>
      <td>0.22</td>
      <td>1.10</td>
    </tr>
  </tbody>
</table>
<p>1683 rows × 3 columns</p>
</div>




```python
#스태킹
print(alco)
tall_alco=alco.stack()
print(tall_alco)
```

                  Beer  Wine  Spirits
    State   Year                     
    Alabama 1977  0.99  0.13     0.84
            1978  0.98  0.12     0.88
            1979  0.98  0.12     0.84
            1980  0.96  0.16     0.74
            1981  1.00  0.19     0.73
    ...            ...   ...      ...
    Wyoming 2005  1.21  0.23     0.97
            2006  1.47  0.23     1.05
            2007  1.49  0.23     1.10
            2008  1.54  0.23     1.12
            2009  1.45  0.22     1.10
    
    [1683 rows x 3 columns]
    State    Year         
    Alabama  1977  Beer       0.99
                   Wine       0.13
                   Spirits    0.84
             1978  Beer       0.98
                   Wine       0.12
                              ... 
    Wyoming  2008  Wine       0.23
                   Spirits    1.12
             2009  Beer       1.45
                   Wine       0.22
                   Spirits    1.10
    Length: 5049, dtype: float64
    


```python
#언스태킹
print(alco.head())
wide_alco = alco.unstack()
print(wide_alco.head())
```

                  Beer  Wine  Spirits
    State   Year                     
    Alabama 1977  0.99  0.13     0.84
            1978  0.98  0.12     0.88
            1979  0.98  0.12     0.84
            1980  0.96  0.16     0.74
            1981  1.00  0.19     0.73
                Beer                                                        ...  \
    Year        1977  1978  1979  1980  1981  1982  1983  1984  1985  1986  ...   
    State                                                                   ...   
    Alabama     0.99  0.98  0.98  0.96  1.00  1.00  1.01  1.02  1.06  1.09  ...   
    Alaska      1.19  1.39  1.50  1.55  1.71  1.75  1.76  1.73  1.68  1.68  ...   
    Arizona     1.70  1.77  1.86  1.69  1.78  1.74  1.62  1.57  1.67  1.77  ...   
    Arkansas    0.92  0.97  0.93  1.00  1.06  1.03  1.03  1.02  1.03  1.06  ...   
    California  1.31  1.36  1.42  1.42  1.43  1.37  1.37  1.38  1.32  1.36  ...   
    
               Spirits                                                        
    Year          2000  2001  2002  2003  2004  2005  2006  2007  2008  2009  
    State                                                                     
    Alabama       0.51  0.53  0.53  0.52  0.52  0.53  0.55  0.56  0.58  0.58  
    Alaska        0.92  0.97  1.08  0.79  0.96  0.99  1.02  1.07  1.09  1.16  
    Arizona       0.71  0.70  0.69  0.71  0.70  0.74  0.78  0.76  0.75  0.74  
    Arkansas      0.53  0.53  0.53  0.56  0.58  0.58  0.59  0.60  0.60  0.60  
    California    0.64  0.64  0.63  0.65  0.67  0.68  0.70  0.72  0.72  0.73  
    
    [5 rows x 99 columns]
    


```python
#피보팅 pivot(index,columns,values)
alco = pd.read_csv("./2020-08/excel/niaaa-report.csv")

alco.pivot("Year","State","Wine").head()
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
      <th>State</th>
      <th>Alabama</th>
      <th>Alaska</th>
      <th>Arizona</th>
      <th>Arkansas</th>
      <th>California</th>
      <th>Colorado</th>
      <th>Connecticut</th>
      <th>Delaware</th>
      <th>District of Columbia</th>
      <th>Florida</th>
      <th>...</th>
      <th>South Dakota</th>
      <th>Tennessee</th>
      <th>Texas</th>
      <th>Utah</th>
      <th>Vermont</th>
      <th>Virginia</th>
      <th>Washington</th>
      <th>West Virginia</th>
      <th>Wisconsin</th>
      <th>Wyoming</th>
    </tr>
    <tr>
      <th>Year</th>
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
      <th>1977</th>
      <td>0.13</td>
      <td>0.42</td>
      <td>0.34</td>
      <td>0.10</td>
      <td>0.67</td>
      <td>0.36</td>
      <td>0.35</td>
      <td>0.24</td>
      <td>0.89</td>
      <td>0.33</td>
      <td>...</td>
      <td>0.17</td>
      <td>0.10</td>
      <td>0.14</td>
      <td>0.14</td>
      <td>0.44</td>
      <td>0.21</td>
      <td>0.45</td>
      <td>0.09</td>
      <td>0.27</td>
      <td>0.21</td>
    </tr>
    <tr>
      <th>1978</th>
      <td>0.12</td>
      <td>0.45</td>
      <td>0.37</td>
      <td>0.11</td>
      <td>0.68</td>
      <td>0.47</td>
      <td>0.38</td>
      <td>0.25</td>
      <td>0.94</td>
      <td>0.34</td>
      <td>...</td>
      <td>0.17</td>
      <td>0.11</td>
      <td>0.14</td>
      <td>0.15</td>
      <td>0.47</td>
      <td>0.21</td>
      <td>0.48</td>
      <td>0.09</td>
      <td>0.28</td>
      <td>0.22</td>
    </tr>
    <tr>
      <th>1979</th>
      <td>0.12</td>
      <td>0.47</td>
      <td>0.39</td>
      <td>0.10</td>
      <td>0.70</td>
      <td>0.47</td>
      <td>0.40</td>
      <td>0.27</td>
      <td>0.99</td>
      <td>0.37</td>
      <td>...</td>
      <td>0.17</td>
      <td>0.11</td>
      <td>0.14</td>
      <td>0.16</td>
      <td>0.47</td>
      <td>0.25</td>
      <td>0.48</td>
      <td>0.09</td>
      <td>0.28</td>
      <td>0.22</td>
    </tr>
    <tr>
      <th>1980</th>
      <td>0.16</td>
      <td>0.50</td>
      <td>0.36</td>
      <td>0.12</td>
      <td>0.71</td>
      <td>0.47</td>
      <td>0.43</td>
      <td>0.29</td>
      <td>0.99</td>
      <td>0.37</td>
      <td>...</td>
      <td>0.18</td>
      <td>0.12</td>
      <td>0.22</td>
      <td>0.14</td>
      <td>0.48</td>
      <td>0.25</td>
      <td>0.52</td>
      <td>0.09</td>
      <td>0.31</td>
      <td>0.24</td>
    </tr>
    <tr>
      <th>1981</th>
      <td>0.19</td>
      <td>0.57</td>
      <td>0.42</td>
      <td>0.12</td>
      <td>0.72</td>
      <td>0.44</td>
      <td>0.44</td>
      <td>0.32</td>
      <td>1.06</td>
      <td>0.39</td>
      <td>...</td>
      <td>0.19</td>
      <td>0.13</td>
      <td>0.24</td>
      <td>0.15</td>
      <td>0.50</td>
      <td>0.27</td>
      <td>0.54</td>
      <td>0.14</td>
      <td>0.31</td>
      <td>0.24</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 51 columns</p>
</div>



## 데이터 누락 다루기
---
> pandas는 결측치를 numpy.nan 을 사용해서 표기하는데 이는 숫자와 달라 혼동을 피할 수 있다.  
또 pandas는 결측치를 탐지하고 보정하는 함수를 제공한다.

**결측치는 반드시 삭제하거나 맥락에 맞는 다른 값으로 교체해서 보정해야한다.**

### 결측치 삭제 
---
> dropna() 함수는 결측치를 가진 열(axis=0,기본값) 이나 행(axis=1)의 일부 (how="any",기본값)
또는 전체 (how="all")를 삭제하고, '정제된' 데이터 프레임 복사본dmf 반환 한다.

**데이터 프레임의 구조자체를 파괴하지 않는 한 결측치만 제거할 수는 없다..**


```python
nan_alco
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
      <th>Beer</th>
      <th>Wine</th>
      <th>Spirits</th>
      <th>Water</th>
    </tr>
    <tr>
      <th>State</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>South Carolina</th>
      <td>1.36</td>
      <td>0.24</td>
      <td>0.77</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>South Dakota</th>
      <td>1.53</td>
      <td>0.22</td>
      <td>0.88</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Samoa</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
nan_alco.dropna(how="all")
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
      <th>Beer</th>
      <th>Wine</th>
      <th>Spirits</th>
      <th>Water</th>
    </tr>
    <tr>
      <th>State</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>South Carolina</th>
      <td>1.36</td>
      <td>0.24</td>
      <td>0.77</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>South Dakota</th>
      <td>1.53</td>
      <td>0.22</td>
      <td>0.88</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
nan_alco.dropna(axis=1,how="all")
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
      <th>Beer</th>
      <th>Wine</th>
      <th>Spirits</th>
    </tr>
    <tr>
      <th>State</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>South Carolina</th>
      <td>1.36</td>
      <td>0.24</td>
      <td>0.77</td>
    </tr>
    <tr>
      <th>South Dakota</th>
      <td>1.53</td>
      <td>0.22</td>
      <td>0.88</td>
    </tr>
    <tr>
      <th>Samoa</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## 결측치 보정
---
> 가장 흔한 보정 방법 두가지는 상수(0,1 등) 와  평균으로 교체하는 것이다.  
우선적으로 insull(),notnull() 함수들을 이용해 어떤 값들이 비어 있는지 파악해야한다.  


```python
sp = nan_alco['Spirits']  #결측 값이 있는 열을 선택
clean= sp.notnull()       #결측 값이 없는 행
sp[-clean]= sp[clean].mean()  #정상적인 값의 평균으로 결측치를 보정한다
nan_alco
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
      <th>Beer</th>
      <th>Wine</th>
      <th>Spirits</th>
      <th>Water</th>
    </tr>
    <tr>
      <th>State</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>South Carolina</th>
      <td>1.36</td>
      <td>0.24</td>
      <td>0.770</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>South Dakota</th>
      <td>1.53</td>
      <td>0.22</td>
      <td>0.880</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Samoa</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.825</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 상수를 이용해 전체 프레임의 결측치 보정
nan_alco.fillna(0)
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
      <th>Beer</th>
      <th>Wine</th>
      <th>Spirits</th>
      <th>Water</th>
    </tr>
    <tr>
      <th>State</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>South Carolina</th>
      <td>1.36</td>
      <td>0.24</td>
      <td>0.770</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>South Dakota</th>
      <td>1.53</td>
      <td>0.22</td>
      <td>0.880</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>Samoa</th>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.825</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
nan_alco.fillna(axis =1,method ="ffill")
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
      <th>Beer</th>
      <th>Wine</th>
      <th>Spirits</th>
      <th>Water</th>
    </tr>
    <tr>
      <th>State</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>South Carolina</th>
      <td>1.36</td>
      <td>0.24</td>
      <td>0.770</td>
      <td>0.770</td>
    </tr>
    <tr>
      <th>South Dakota</th>
      <td>1.53</td>
      <td>0.22</td>
      <td>0.880</td>
      <td>0.880</td>
    </tr>
    <tr>
      <th>Samoa</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.825</td>
      <td>0.825</td>
    </tr>
  </tbody>
</table>
</div>



### 데이터 결합
- 일대일 결합 : 왼쪽 데이터 프레임의 각 행이 오른쪽 데이터 프레임의 행과 하나만 매칭
- 일대다 결합 : 왼쪽 데이터 프레임의 각 행이 오른쪽 데이터 프레임의 행과 2개이상 매칭

각 데이터 프레임에서 여러행이 겹칠 때는 다대닫 결합으로 마찬가지로 pandas는 필요한 만큼 행을 복제하고, '빈곳'에는 numpy.nan 을 집어넣는다.


```python
population = pd.read_csv('./2020-08/excel/population.csv',index_col="State")
population.head()
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
      <th>Population</th>
    </tr>
    <tr>
      <th>State</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama</th>
      <td>4,780,131</td>
    </tr>
    <tr>
      <th>Alaska</th>
      <td>710,249</td>
    </tr>
    <tr>
      <th>Arizona</th>
      <td>6,392,301</td>
    </tr>
    <tr>
      <th>Arkansas</th>
      <td>2,916,025</td>
    </tr>
    <tr>
      <th>California</th>
      <td>37,254,522</td>
    </tr>
  </tbody>
</table>
</div>




```python
alco2009.head()
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
      <th>Beer</th>
      <th>Wine</th>
      <th>Spirits</th>
    </tr>
    <tr>
      <th>State</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama</th>
      <td>1.20</td>
      <td>0.22</td>
      <td>0.58</td>
    </tr>
    <tr>
      <th>Alaska</th>
      <td>1.31</td>
      <td>0.54</td>
      <td>1.16</td>
    </tr>
    <tr>
      <th>Arizona</th>
      <td>1.19</td>
      <td>0.38</td>
      <td>0.74</td>
    </tr>
    <tr>
      <th>Arkansas</th>
      <td>1.07</td>
      <td>0.17</td>
      <td>0.60</td>
    </tr>
    <tr>
      <th>California</th>
      <td>1.05</td>
      <td>0.55</td>
      <td>0.73</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.merge(alco2009.reset_index(),population.reset_index()).set_index("State")
df.head()
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
      <th>Beer</th>
      <th>Wine</th>
      <th>Spirits</th>
      <th>Population</th>
    </tr>
    <tr>
      <th>State</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama</th>
      <td>1.20</td>
      <td>0.22</td>
      <td>0.58</td>
      <td>4,780,131</td>
    </tr>
    <tr>
      <th>Alaska</th>
      <td>1.31</td>
      <td>0.54</td>
      <td>1.16</td>
      <td>710,249</td>
    </tr>
    <tr>
      <th>Arizona</th>
      <td>1.19</td>
      <td>0.38</td>
      <td>0.74</td>
      <td>6,392,301</td>
    </tr>
    <tr>
      <th>Arkansas</th>
      <td>1.07</td>
      <td>0.17</td>
      <td>0.60</td>
      <td>2,916,025</td>
    </tr>
    <tr>
      <th>California</th>
      <td>1.05</td>
      <td>0.55</td>
      <td>0.73</td>
      <td>37,254,522</td>
    </tr>
  </tbody>
</table>
</div>



## 데이터 붙이기
> concat() 함수는 수직이나 수평 축을 따라 여러 데이트 프레임을 이어 붙인 새로운 데이터 프레임을 반환.


```python
pd.concat([alco2009,population],axis=1).head() 
#축이 일치하지 않으면 pandas 가 '빈곳'에 결측치가 채워진 행이나 열을 새로 추가한다.
```

## 중복제거
---
- duplicated([subset]) 함수
    - 각 행의 전체 혹은 일부(subset) 열이 중복됐는지를 의미하는 불시리즈를 반환  
    - 옵셔널 파라미터 keep으로 중복된 항목의 원본을 첫 번째('first')행으로 할지, 마지막('last') 행으로 할지, 중복된 모든 항목을 제거할지(False) 결정 할 수 있다.
- drop_duplicated() 함수
    - 전체나 일부(subset) 중복된 열이 제거된 데이터 프레임이나 시리즈의 복사본을 반환
    - duplicated([subset])  함수와 마찬가지로 옵셔널 파라미터 적용가능
    - 옵셔널 파라미터 inplace = True를 사용해 원본 데이터 프레임에서 중복된 항목 제거가능

## 데이터 정렬하기
- sort_index() 함수는 인덱스로 정렬된 데이터프레임을 반환, ascending 파라미터로 순서 조정 가능
- sort_values() 함수는 값으로 정렬한 데이터 프레임이나 시리즈 반환
    - 데이터 프레임에서 첫 번째 파라미터는 열이나 열 리스트이며, 옵셔널 파라미터 ascending은 불 값이나 불 리스트다.
    - nan_position 파라미터(first 나 last)는 nan을 어디에 저장할지 결정한다.
- rank() 함수는 데이터프레임이나 시리즈 값에서 숫자로 된 순위를 계산한다


```python
population.sort_index().head()
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
      <th>Population</th>
    </tr>
    <tr>
      <th>State</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama</th>
      <td>4,780,131</td>
    </tr>
    <tr>
      <th>Alaska</th>
      <td>710,249</td>
    </tr>
    <tr>
      <th>Arizona</th>
      <td>6,392,301</td>
    </tr>
    <tr>
      <th>Arkansas</th>
      <td>2,916,025</td>
    </tr>
    <tr>
      <th>California</th>
      <td>37,254,522</td>
    </tr>
  </tbody>
</table>
</div>




```python
population.sort_values("Population").head()
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
      <th>Population</th>
    </tr>
    <tr>
      <th>State</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Rhode Island</th>
      <td>1,052,940</td>
    </tr>
    <tr>
      <th>New Hampshire</th>
      <td>1,316,461</td>
    </tr>
    <tr>
      <th>Maine</th>
      <td>1,328,364</td>
    </tr>
    <tr>
      <th>Hawaii</th>
      <td>1,360,301</td>
    </tr>
    <tr>
      <th>Idaho</th>
      <td>1,567,650</td>
    </tr>
  </tbody>
</table>
</div>




```python
pop_by_state = population.sort_index()
pop_by_state.rank().head()
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
      <th>Population</th>
    </tr>
    <tr>
      <th>State</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama</th>
      <td>28.0</td>
    </tr>
    <tr>
      <th>Alaska</th>
      <td>43.0</td>
    </tr>
    <tr>
      <th>Arizona</th>
      <td>36.0</td>
    </tr>
    <tr>
      <th>Arkansas</th>
      <td>17.0</td>
    </tr>
    <tr>
      <th>California</th>
      <td>24.0</td>
    </tr>
  </tbody>
</table>
</div>



## 기술 통계
---
> 기술 통계 함수는 시리즈나 데이터 프레임의 각 열에서 sum(), mean(), meadian(), std(), count(), min(), max() 함수의 값을 계산한다.


```python
alco2009.max()
```




    Beer       1.72
    Wine       1.00
    Spirits    1.82
    dtype: float64




```python
alco2009.min(axis=1)
```




    State
    Alabama                 0.22
    Alaska                  0.54
    Arizona                 0.38
    Arkansas                0.17
    California              0.55
    Colorado                0.46
    Connecticut             0.59
    Delaware                0.57
    District of Columbia    1.00
    Florida                 0.48
    Georgia                 0.25
    Hawaii                  0.53
    Idaho                   0.70
    Illinois                0.39
    Indiana                 0.25
    Iowa                    0.18
    Kansas                  0.14
    Kentucky                0.18
    Louisiana               0.28
    Maine                   0.42
    Maryland                0.37
    Massachusetts           0.61
    Michigan                0.31
    Minnesota               0.37
    Mississippi             0.11
    Missouri                0.30
    Montana                 0.45
    Nebraska                0.20
    Nevada                  0.58
    New Hampshire           0.84
    New Jersey              0.57
    New Mexico              0.32
    New York                0.46
    North Carolina          0.34
    North Dakota            0.25
    Ohio                    0.26
    Oklahoma                0.18
    Oregon                  0.49
    Pennsylvania            0.23
    Rhode Island            0.53
    South Carolina          0.24
    South Dakota            0.22
    Tennessee               0.21
    Texas                   0.28
    Utah                    0.17
    Vermont                 0.63
    Virginia                0.43
    Washington              0.51
    West Virginia           0.10
    Wisconsin               0.31
    Wyoming                 0.22
    dtype: float64




```python
alco2009.sum()
```




    Beer       63.22
    Wine       19.59
    Spirits    41.81
    dtype: float64



## 고유값, 카운팅, 멤버십
---
>numpy는 배열을 셋으로 취급할 수 있다. pandas도 시리즈를 셋으로 취급할 수 있다.  
- unique()와 value_counts() 함수는 각각 시리즈와 데이터 프레임에서 고유한 값으로 구성 된 배열을 만들고, 각 고유 값의 등장 빈도를 계산한다.  
- 시리즈가 nan 값을 포함한다면 그 역시도 빈도 카운팅에 포함 할 수 있다.
- isin() 함수는 시리즈와 데이터 프레임의 각 아이템이 특정 묶음에 속하는지 여부를 불 형식으로 반환한다


```python
dna='agtatagcgcgtagaccgt'
dna=dna.upper()

dna_as_series = pd.Series(list(dna),name="genes")
dna_as_series.head()
```




    0    A
    1    G
    2    T
    3    A
    4    T
    Name: genes, dtype: object




```python
print(dna_as_series.unique())
print(dna_as_series.value_counts().sort_index())
```

    ['A' 'G' 'T' 'C']
    A    5
    C    4
    G    6
    T    4
    Name: genes, dtype: int64
    


```python
valid_nucs= list("ACGT")
dna_as_series.isin(valid_nucs).head()                 
```




    0    True
    1    True
    2    True
    3    True
    4    True
    Name: genes, dtype: bool



## 데이터 변환하기
---
> 사칙연산차
- pandas 는 사칙 연산자와 numpy 유니버셜 함수를 지원한다


```python
alco = alco.set_index(["State","Year"])
alco['Total'] =alco.Beer+alco.Wine+alco.Spirits
alco.head()
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
      <th></th>
      <th>Beer</th>
      <th>Wine</th>
      <th>Spirits</th>
      <th>Total</th>
    </tr>
    <tr>
      <th>State</th>
      <th>Year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">Alabama</th>
      <th>1977</th>
      <td>0.99</td>
      <td>0.13</td>
      <td>0.84</td>
      <td>1.96</td>
    </tr>
    <tr>
      <th>1978</th>
      <td>0.98</td>
      <td>0.12</td>
      <td>0.88</td>
      <td>1.98</td>
    </tr>
    <tr>
      <th>1979</th>
      <td>0.98</td>
      <td>0.12</td>
      <td>0.84</td>
      <td>1.94</td>
    </tr>
    <tr>
      <th>1980</th>
      <td>0.96</td>
      <td>0.16</td>
      <td>0.74</td>
      <td>1.86</td>
    </tr>
    <tr>
      <th>1981</th>
      <td>1.00</td>
      <td>0.19</td>
      <td>0.73</td>
      <td>1.92</td>
    </tr>
  </tbody>
</table>
</div>



## 데이터 집계
---
> 데이터 집계는 데이터를 분리하고 적용하고 결합하는 세 단계로 구성된다
 1. 분리 단계에서는 키(key)를 사용해서 데이터를 여러 덩어리로 분리한다.
 2. 적용 단계에서는 각 덩어리에 집계 함수(sum() 이나 count() 함수 등을) 적용 한다.
 3. 결합 단계에서는 산출한 결과를 새로운 시리즈나 데이터 프레임에 담는다.

집계 함수에는 다음 함수들이 있다.  
count() , sum() , mean() , median(), std(), var(), min(), max(), prod(), first(),last()


```python
alco_noidx = alco.reset_index()
sum_alco = alco_noidx.groupby("Year").sum()
sum_alco.tail()
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
      <th>Beer</th>
      <th>Wine</th>
      <th>Spirits</th>
      <th>Total</th>
    </tr>
    <tr>
      <th>Year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2005</th>
      <td>63.49</td>
      <td>18.06</td>
      <td>38.89</td>
      <td>120.44</td>
    </tr>
    <tr>
      <th>2006</th>
      <td>64.37</td>
      <td>18.66</td>
      <td>40.15</td>
      <td>123.18</td>
    </tr>
    <tr>
      <th>2007</th>
      <td>64.67</td>
      <td>19.08</td>
      <td>40.97</td>
      <td>124.72</td>
    </tr>
    <tr>
      <th>2008</th>
      <td>64.67</td>
      <td>19.41</td>
      <td>41.59</td>
      <td>125.67</td>
    </tr>
    <tr>
      <th>2009</th>
      <td>63.22</td>
      <td>19.59</td>
      <td>41.81</td>
      <td>124.62</td>
    </tr>
  </tbody>
</table>
</div>



### 매핑 
> 가장 일반적인 형태의 데이터 변환
- map() 함수를 사용해 인자가 1개인 임의의 함수를 선택한 열의 모든 엘리먼트에 적용
- 전달하는 함수는 파이썬 내장 함수나 임포트한 모듈의 함수, 사용자가 정의한 함수 등이 될 수 있다.


```python
# 세글가 약어로 된 주 이름을 만들어 보자

with_state = alco2009.reset_index()
abbrevs = with_state["State"].map(lambda x:x[:3].upper())
abbrevs.head()
```




    0    ALA
    1    ALA
    2    ARI
    3    ARK
    4    CAL
    Name: State, dtype: object



### 교차 집계
> 교차 집계는 그룹별 빈도를 산출하고 다른 두 카테고리 변수를 표현하는 행과 열로 된 데이터 프레임을 반환한다. 옵셔널 파라미터 margins = True 설정하면 이 함수는 행과 열의 소계도 계산한다.


```python
wine_state = alco2009['Wine']>alco2009['Wine'].mean()
beer_state = alco2009['Beer']>alco2009['Beer'].mean()
pd.crosstab(wine_state,beer_state) 
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
      <th>Beer</th>
      <th>False</th>
      <th>True</th>
    </tr>
    <tr>
      <th>Wine</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>False</th>
      <td>14</td>
      <td>15</td>
    </tr>
    <tr>
      <th>True</th>
      <td>12</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.crosstab(wine_state,beer_state,margins=True)
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
      <th>Beer</th>
      <th>False</th>
      <th>True</th>
      <th>All</th>
    </tr>
    <tr>
      <th>Wine</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>False</th>
      <td>14</td>
      <td>15</td>
      <td>29</td>
    </tr>
    <tr>
      <th>True</th>
      <td>12</td>
      <td>10</td>
      <td>22</td>
    </tr>
    <tr>
      <th>All</th>
      <td>26</td>
      <td>25</td>
      <td>51</td>
    </tr>
  </tbody>
</table>
</div>



# Pandas 의 파일 입출력 다루기

>pandas는 다음 기능을 제공한다
- 자동 인덱싱 및 열 이름 추출
- 데이터 타입 추론, 데이터변환, 결측치 탐지
- 날짜 및 시간 파싱
- 불필요한 데이터 제거(행,각주,주석 건너뛰기 : 천 단위 구분자 처리)
- 데이터 묶기


##### read_csv() 함수는 지정된 파일명이나 파일 핸들에서 데이터 프레임을 읽어온다.
> read_csv()의 옵셔널 파라미터
- sep 또는 delimiter : 열 구분자. 정규표현식도 인자로 처리가능
- header : 열로 사용할 행 넘버. 별도의 열 이름 리스트가 있다면 None을 전달 한다.
- index_col : 인덱스로 사용할 열 이름. False를 전달하면 pandas가 기본 수치형 인덱스 생성
- skiprows : 파일에서 생략해야 할 첫 n번째 행이나 행 넘버 리스트
- thousands : 큰 숫자에서 천 단위 구분을 하는데 사용된 문자
- names : 열 이름 리스트
- na_values : 결측치로서 처리할 문자열이나 문자열 리스트. 
