# 🛍️ Анализ покупок в магазине

Простой проект на Python с использованием pandas для анализа данных о покупках.

## 📋 Описание

Проект позволяет:

- посчитать общую выручку;
- сгруппировать товары по категориям;
- найти дорогие покупки;
- вычислить среднюю цену по категориям;
- определить категорию с наибольшим количеством проданных товаров.

## 🗂️ Пример структуры данных

```python
purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]
```
## Результат

Общая выручка: 23.5

Товары по категориям: {'bakery': ['bread'], 'dairy': ['milk'], 'fruit': ['apple', 'banana']}

Покупки дороже 1: [{'item': 'apple', 'category': 'fruit', 'price': 1.2, 'quantity': 10}, {'item': 'milk', 'category': 'dairy', 'price': 1.5, 'quantity': 2}, {'item': 'bread', 'category': 'bakery', 'price': 2.0, 'quantity': 3}]

Средняя цена по категориям: {'bakery': 2.0, 'dairy': 1.5, 'fruit': 0.85}

Категория с наибольшим количеством проданных товаров: fruit
