

# 데이터 전처리
---

## item_price 피처 
---
itme_price 피처를 살펴보면 가격앞에 $ 문자가 잇다. 수치형 데이터로 변환하기 위해서는 $ 문자를 제거해야 한다.


```python
chipo['item_price'].head()
```




    0     $2.39 
    1     $3.39 
    2     $3.39 
    3     $2.39 
    4    $16.98 
    Name: item_price, dtype: object




```python
chipo['item_price']=chipo['item_price'].apply(lambda x : float(x[1:]))
chipo['item_price'].head()
```




    0     2.39
    1     3.39
    2     3.39
    3     2.39
    4    16.98
    Name: item_price, dtype: float64



# 탐색적 분석

## 주문당 평균 계산 금액 출력하기 
---
1. order_id로 그룹 생성
2. item_price 피처에 sum() 함수를 적용
3. mean() 함수를 추가


```python
chipo.groupby('order_id')['item_price'].sum().mean()
```




    18.81142857142869



## 한 주문에 10 달러 이상 지불한 주문 번호 출력
---



```python
chipo.head()
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
      <td>2.39</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>Izze</td>
      <td>[Clementine]</td>
      <td>3.39</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>1</td>
      <td>Nantucket Nectar</td>
      <td>[Apple]</td>
      <td>3.39</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>Chips and Tomatillo-Green Chili Salsa</td>
      <td>NaN</td>
      <td>2.39</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>2</td>
      <td>Chicken Bowl</td>
      <td>[Tomatillo-Red Chili Salsa (Hot), [Black Beans...</td>
      <td>16.98</td>
    </tr>
  </tbody>
</table>
</div>




```python
chipo_order_id_group = chipo.groupby('order_id').sum()
result = chipo_order_id_group[chipo_order_id_group['item_price']>10]
result
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
      <th>quantity</th>
      <th>item_price</th>
    </tr>
    <tr>
      <th>order_id</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>11.56</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>16.98</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>12.67</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>21.00</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>13.70</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1830</th>
      <td>2</td>
      <td>23.00</td>
    </tr>
    <tr>
      <th>1831</th>
      <td>3</td>
      <td>12.90</td>
    </tr>
    <tr>
      <th>1832</th>
      <td>2</td>
      <td>13.20</td>
    </tr>
    <tr>
      <th>1833</th>
      <td>2</td>
      <td>23.50</td>
    </tr>
    <tr>
      <th>1834</th>
      <td>3</td>
      <td>28.75</td>
    </tr>
  </tbody>
</table>
<p>1834 rows × 2 columns</p>
</div>



## 각 아이템의 가격 구하기
---


```python
# 동일 아이템을 1개만 구매한 주문 선별
chipo.head()
chipo_one_item = chipo[chipo['quantity']==1]

# group by를 이용해 item_name 별로 묶고, 각 아이템의 최저가 계산

price_per_item = chipo_one_item.groupby('item_name').min()

#item_price를 내림차순으로 정렬
price_per_item.sort_values(by = 'item_price',ascending=False)
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
      <th>order_id</th>
      <th>quantity</th>
      <th>choice_description</th>
      <th>item_price</th>
    </tr>
    <tr>
      <th>item_name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Steak Salad Bowl</th>
      <td>250</td>
      <td>1</td>
      <td>[Fresh Tomato Salsa, Lettuce]</td>
      <td>9.39</td>
    </tr>
    <tr>
      <th>Barbacoa Salad Bowl</th>
      <td>501</td>
      <td>1</td>
      <td>[Fresh Tomato Salsa, Guacamole]</td>
      <td>9.39</td>
    </tr>
    <tr>
      <th>Carnitas Salad Bowl</th>
      <td>468</td>
      <td>1</td>
      <td>[Fresh Tomato Salsa, [Rice, Black Beans, Chees...</td>
      <td>9.39</td>
    </tr>
    <tr>
      <th>Carnitas Soft Tacos</th>
      <td>103</td>
      <td>1</td>
      <td>[Fresh Tomato Salsa (Mild), [Black Beans, Rice...</td>
      <td>8.99</td>
    </tr>
    <tr>
      <th>Carnitas Crispy Tacos</th>
      <td>230</td>
      <td>1</td>
      <td>[Fresh Tomato Salsa, [Fajita Vegetables, Rice,...</td>
      <td>8.99</td>
    </tr>
    <tr>
      <th>Steak Soft Tacos</th>
      <td>4</td>
      <td>1</td>
      <td>[Fresh Tomato Salsa (Mild), [Cheese, Sour Cream]]</td>
      <td>8.99</td>
    </tr>
    <tr>
      <th>Carnitas Salad</th>
      <td>1500</td>
      <td>1</td>
      <td>[[Fresh Tomato Salsa (Mild), Roasted Chili Cor...</td>
      <td>8.99</td>
    </tr>
    <tr>
      <th>Carnitas Bowl</th>
      <td>17</td>
      <td>1</td>
      <td>[Fresh Tomato (Mild), [Guacamole, Lettuce, Ric...</td>
      <td>8.99</td>
    </tr>
    <tr>
      <th>Barbacoa Soft Tacos</th>
      <td>26</td>
      <td>1</td>
      <td>[Fresh Tomato Salsa, [Black Beans, Cheese, Let...</td>
      <td>8.99</td>
    </tr>
    <tr>
      <th>Barbacoa Crispy Tacos</th>
      <td>75</td>
      <td>1</td>
      <td>[Fresh Tomato Salsa, Guacamole]</td>
      <td>8.99</td>
    </tr>
    <tr>
      <th>Veggie Salad Bowl</th>
      <td>83</td>
      <td>1</td>
      <td>[Fresh Tomato Salsa, [Fajita Vegetables, Black...</td>
      <td>8.75</td>
    </tr>
    <tr>
      <th>Chicken Salad Bowl</th>
      <td>20</td>
      <td>1</td>
      <td>[Fresh Tomato Salsa, Fajita Vegetables]</td>
      <td>8.75</td>
    </tr>
    <tr>
      <th>Steak Burrito</th>
      <td>4</td>
      <td>1</td>
      <td>[Brown Rice]</td>
      <td>8.69</td>
    </tr>
    <tr>
      <th>Steak Crispy Tacos</th>
      <td>40</td>
      <td>1</td>
      <td>[Fresh Tomato (Mild), [Lettuce, Cheese]]</td>
      <td>8.69</td>
    </tr>
    <tr>
      <th>Steak Salad</th>
      <td>276</td>
      <td>1</td>
      <td>[Fresh Tomato Salsa (Mild), [Rice, Cheese, Sou...</td>
      <td>8.69</td>
    </tr>
    <tr>
      <th>Carnitas Burrito</th>
      <td>14</td>
      <td>1</td>
      <td>[Fresh Tomato (Mild), [Lettuce, Black Beans, G...</td>
      <td>8.69</td>
    </tr>
    <tr>
      <th>Steak Bowl</th>
      <td>25</td>
      <td>1</td>
      <td>[Fresh Tomato (Mild), [Guacamole, Lettuce, Pin...</td>
      <td>8.69</td>
    </tr>
    <tr>
      <th>Barbacoa Burrito</th>
      <td>11</td>
      <td>1</td>
      <td>[Fresh Tomato (Mild), [Black Beans, Rice, Sour...</td>
      <td>8.69</td>
    </tr>
    <tr>
      <th>Barbacoa Bowl</th>
      <td>19</td>
      <td>1</td>
      <td>[Fresh Tomato (Mild), [Lettuce, Black Beans, R...</td>
      <td>8.69</td>
    </tr>
    <tr>
      <th>Chicken Soft Tacos</th>
      <td>6</td>
      <td>1</td>
      <td>[Fresh Tomato Salsa (Mild), [Black Beans, Rice...</td>
      <td>8.49</td>
    </tr>
    <tr>
      <th>Veggie Bowl</th>
      <td>28</td>
      <td>1</td>
      <td>[Fresh Tomato Salsa (Mild), [Pinto Beans, Blac...</td>
      <td>8.49</td>
    </tr>
    <tr>
      <th>Veggie Burrito</th>
      <td>26</td>
      <td>1</td>
      <td>[Fresh Tomato Salsa (Mild), [Black Beans, Faji...</td>
      <td>8.49</td>
    </tr>
    <tr>
      <th>Veggie Soft Tacos</th>
      <td>304</td>
      <td>1</td>
      <td>[Fresh Tomato Salsa (Mild), [Pinto Beans, Rice...</td>
      <td>8.49</td>
    </tr>
    <tr>
      <th>Chicken Crispy Tacos</th>
      <td>6</td>
      <td>1</td>
      <td>[Fresh Tomato Salsa (Mild), Fajita Veggies]</td>
      <td>8.49</td>
    </tr>
    <tr>
      <th>Veggie Crispy Tacos</th>
      <td>668</td>
      <td>1</td>
      <td>[Fresh Tomato Salsa (Mild), [Pinto Beans, Rice...</td>
      <td>8.49</td>
    </tr>
    <tr>
      <th>Veggie Salad</th>
      <td>686</td>
      <td>1</td>
      <td>[Roasted Chili Corn Salsa (Medium), [Black Bea...</td>
      <td>8.49</td>
    </tr>
    <tr>
      <th>Chicken Salad</th>
      <td>109</td>
      <td>1</td>
      <td>[Fresh Tomato Salsa (Mild), Black Beans]</td>
      <td>8.19</td>
    </tr>
    <tr>
      <th>Chicken Burrito</th>
      <td>8</td>
      <td>1</td>
      <td>[Fresh Tomato (Mild), [Black Beans, Rice, Sour...</td>
      <td>8.19</td>
    </tr>
    <tr>
      <th>Chicken Bowl</th>
      <td>3</td>
      <td>1</td>
      <td>[Fresh Tomato (Mild), [Guacamole, Rice]]</td>
      <td>8.19</td>
    </tr>
    <tr>
      <th>Crispy Tacos</th>
      <td>217</td>
      <td>1</td>
      <td>[Adobo-Marinated and Grilled Chicken]</td>
      <td>7.40</td>
    </tr>
    <tr>
      <th>Burrito</th>
      <td>214</td>
      <td>1</td>
      <td>[Adobo-Marinated and Grilled Chicken, Pinto Be...</td>
      <td>7.40</td>
    </tr>
    <tr>
      <th>Bowl</th>
      <td>279</td>
      <td>1</td>
      <td>[Adobo-Marinated and Grilled Steak, [Sour Crea...</td>
      <td>7.40</td>
    </tr>
    <tr>
      <th>Salad</th>
      <td>575</td>
      <td>1</td>
      <td>[Brown Rice, Adobo-Marinated and Grilled Chick...</td>
      <td>7.40</td>
    </tr>
    <tr>
      <th>6 Pack Soft Drink</th>
      <td>129</td>
      <td>1</td>
      <td>[Coke]</td>
      <td>6.49</td>
    </tr>
    <tr>
      <th>Chips and Guacamole</th>
      <td>5</td>
      <td>1</td>
      <td>NaN</td>
      <td>3.89</td>
    </tr>
    <tr>
      <th>Izze</th>
      <td>1</td>
      <td>1</td>
      <td>[Blackberry]</td>
      <td>3.39</td>
    </tr>
    <tr>
      <th>Nantucket Nectar</th>
      <td>1</td>
      <td>1</td>
      <td>[Apple]</td>
      <td>3.39</td>
    </tr>
    <tr>
      <th>Chips and Mild Fresh Tomato Salsa</th>
      <td>279</td>
      <td>1</td>
      <td>NaN</td>
      <td>3.00</td>
    </tr>
    <tr>
      <th>Chips and Tomatillo Red Chili Salsa</th>
      <td>49</td>
      <td>1</td>
      <td>NaN</td>
      <td>2.95</td>
    </tr>
    <tr>
      <th>Chips and Tomatillo Green Chili Salsa</th>
      <td>18</td>
      <td>1</td>
      <td>NaN</td>
      <td>2.95</td>
    </tr>
    <tr>
      <th>Chips and Roasted Chili Corn Salsa</th>
      <td>102</td>
      <td>1</td>
      <td>NaN</td>
      <td>2.95</td>
    </tr>
    <tr>
      <th>Chips and Tomatillo-Red Chili Salsa</th>
      <td>130</td>
      <td>1</td>
      <td>NaN</td>
      <td>2.39</td>
    </tr>
    <tr>
      <th>Chips and Tomatillo-Green Chili Salsa</th>
      <td>1</td>
      <td>1</td>
      <td>NaN</td>
      <td>2.39</td>
    </tr>
    <tr>
      <th>Chips and Roasted Chili-Corn Salsa</th>
      <td>85</td>
      <td>1</td>
      <td>NaN</td>
      <td>2.39</td>
    </tr>
    <tr>
      <th>Chips and Fresh Tomato Salsa</th>
      <td>1</td>
      <td>1</td>
      <td>NaN</td>
      <td>2.29</td>
    </tr>
    <tr>
      <th>Chips</th>
      <td>19</td>
      <td>1</td>
      <td>NaN</td>
      <td>1.99</td>
    </tr>
    <tr>
      <th>Side of Chips</th>
      <td>3</td>
      <td>1</td>
      <td>NaN</td>
      <td>1.69</td>
    </tr>
    <tr>
      <th>Canned Soft Drink</th>
      <td>114</td>
      <td>1</td>
      <td>[Coke]</td>
      <td>1.25</td>
    </tr>
    <tr>
      <th>Canned Soda</th>
      <td>14</td>
      <td>1</td>
      <td>[Coca Cola]</td>
      <td>1.09</td>
    </tr>
    <tr>
      <th>Bottled Water</th>
      <td>17</td>
      <td>1</td>
      <td>NaN</td>
      <td>1.09</td>
    </tr>
  </tbody>
</table>
</div>



## 가장 비싼 주문에서 아이템이 총 몇개 팔렸는지 확인
---
order_id 그룹별 합계 연산 적용후 item_price를 기준으로 sort_values 반환


```python
chipo.groupby('order_id').sum().sort_values('item_price',ascending=False)
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
      <th>quantity</th>
      <th>item_price</th>
    </tr>
    <tr>
      <th>order_id</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>926</th>
      <td>23</td>
      <td>205.25</td>
    </tr>
    <tr>
      <th>1443</th>
      <td>35</td>
      <td>160.74</td>
    </tr>
    <tr>
      <th>1483</th>
      <td>14</td>
      <td>139.00</td>
    </tr>
    <tr>
      <th>691</th>
      <td>11</td>
      <td>118.25</td>
    </tr>
    <tr>
      <th>1786</th>
      <td>20</td>
      <td>114.30</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2</td>
      <td>10.08</td>
    </tr>
    <tr>
      <th>889</th>
      <td>2</td>
      <td>10.08</td>
    </tr>
    <tr>
      <th>1014</th>
      <td>2</td>
      <td>10.08</td>
    </tr>
    <tr>
      <th>1303</th>
      <td>2</td>
      <td>10.08</td>
    </tr>
    <tr>
      <th>1602</th>
      <td>2</td>
      <td>10.08</td>
    </tr>
  </tbody>
</table>
<p>1834 rows × 2 columns</p>
</div>



## 'Chicken Bowl' 이 몇번 주문 되었는지 구하기
---


```python
chipo_chicken = chipo[chipo['item_name']=='Chicken Bowl']

# 한 주문 내에서 중복 집계된 item_name 제거
chipo_chicken = chipo_chicken.drop_duplicates(['item_name','order_id'])
print(len(chipo_chicken))
```

    615
    
