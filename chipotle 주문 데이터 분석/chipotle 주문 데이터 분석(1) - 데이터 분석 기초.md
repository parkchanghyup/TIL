# 데이터 불러오기 
---



```python
import pandas as pd
chipo = pd.read_csv('C:/Users/ariz/Desktop/슬기로운 방학생활/이것이 데이터 분석이다/data/chipotle.tsv',sep='\t')
print(chipo.shape)
print('---------------------------------')
print(chipo.info())      
chipo.head()
```

    (4622, 5)
    ---------------------------------
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 4622 entries, 0 to 4621
    Data columns (total 5 columns):
     #   Column              Non-Null Count  Dtype 
    ---  ------              --------------  ----- 
     0   order_id            4622 non-null   int64 
     1   quantity            4622 non-null   int64 
     2   item_name           4622 non-null   object
     3   choice_description  3376 non-null   object
     4   item_price          4622 non-null   object
    dtypes: int64(2), object(3)
    memory usage: 180.7+ KB
    None
    




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
      <th>order_id</th>
      <th>quantity</th>
      <th>item_name</th>
      <th>choice_description</th>
      <th>item_price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>Chips and Fresh Tomato Salsa</td>
      <td>NaN</td>
      <td>$2.39</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>Izze</td>
      <td>[Clementine]</td>
      <td>$3.39</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>1</td>
      <td>Nantucket Nectar</td>
      <td>[Apple]</td>
      <td>$3.39</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>Chips and Tomatillo-Green Chili Salsa</td>
      <td>NaN</td>
      <td>$2.39</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>2</td>
      <td>Chicken Bowl</td>
      <td>[Tomatillo-Red Chili Salsa (Hot), [Black Beans...</td>
      <td>$16.98</td>
    </tr>
  </tbody>
</table>
</div>



chipo 데이터는 4622개의  행과 5개의 컬럼으로 구성되어 있다.    
그리고 choice_description 컬럼에는 결측치가 약 1300개 존재 한다.  
또 order_id 컬럼은 id 컬럼이므로 int 형이아닌 str 형으로 변경이 필요 해보인다. 
먼저 order_id 컬럼 부터 변경 해보자.


```python
# order_id 컬럼 데이터 형 변환

chipo['order_id'] = chipo['order_id'].astype('str')
print(chipo.info())
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 4622 entries, 0 to 4621
    Data columns (total 5 columns):
     #   Column              Non-Null Count  Dtype 
    ---  ------              --------------  ----- 
     0   order_id            4622 non-null   object
     1   quantity            4622 non-null   int64 
     2   item_name           4622 non-null   object
     3   choice_description  3376 non-null   object
     4   item_price          4622 non-null   object
    dtypes: int64(1), object(4)
    memory usage: 180.7+ KB
    None
    

### describe() 함수로 기초 통계량 출력
---

describe() 함수는 데이터 형이 실수나 정수인 데이테 에대해 기초 통계량을 출력해준다.


```python
print(chipo.describe())
```

              quantity
    count  4622.000000
    mean      1.075725
    std       0.410186
    min       1.000000
    25%       1.000000
    50%       1.000000
    75%       1.000000
    max      15.000000
    

### order_id와 item_name의 개수 출력
---
unique() 함수는 컬럼의 데이터에서 중복을 제외하고 반환 한다 .


```python
print(len(chipo['order_id'].unique()))
print(len(chipo['item_name'].unique()))
```

    1834
    50
    
