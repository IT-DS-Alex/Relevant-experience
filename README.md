# Стоимость поддержанного автомобиля
Предсказание стоимости автомобиля на вторичном рынке.

## Описание задачи
Многие знают про маркетплейсы где продаются б/у вещи, на которых есть возможность недорого купить качественную и полезную вещь. Но всегда волнует вопрос - кто и как устанавливает цену, и какие его характеристики больше всего влияют на итоговую стоимость продажи?! Вопрос становиться особо актуальным, если речь идет про дорогие товары, например про автомобили!

Целью проекта будет разработанная модель предсказания стоимости автомобиля на вторичном рынке.

## Описание данных
'year' - год производства

'make' - производитель

'model' - модель

'trim' - модификация

'body' - тип кузова

'transmission' - тип КПП

'vin' - идентификатор (вин)

'state' - штат регистрации

'condition' - состояние по шкале (1-5)

'odometer' - пробег

'color' - цвет кузова

'interior' - цвет интерьера

'seller' - продавец

'sellingprice' - стоимость продажи

'saledate' - дата продажи

## Примечаниe:
Для оценки качества моделей применяем метрику MAPE.

Data columns (total 15 columns):
 #   Column        Non-Null Count   Dtype  
---  ------        --------------   -----  
 0   year          440236 non-null  int64  
 1   make          432193 non-null  object 
 2   model         432113 non-null  object 
 3   trim          431899 non-null  object 
 4   body          429843 non-null  object 
 5   transmission  388775 non-null  object 
 6   vin           440236 non-null  object 
 7   state         440236 non-null  object 
 8   condition     430831 non-null  float64
 9   odometer      440167 non-null  float64
 10  color         439650 non-null  object 
 11  interior      439650 non-null  object 
 12  seller        440236 non-null  object 
 13  sellingprice  440236 non-null  int64  
 14  saledate      440236 non-null  object 

 
