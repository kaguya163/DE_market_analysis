import pandas as pd

purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]
    
df = pd.DataFrame(purchases)

def total_revenue(purchases):
    df = pd.DataFrame(purchases)
    return (df.price * df.quantity).sum()

def items_by_category(purchases):
    df = pd.DataFrame(purchases)
    result = df.groupby('category')['item'].unique().to_dict()
    result = {k: list(v) for k, v in result.items()}
    return result

def expensive_purchases(purchases, min_price):
    df = pd.DataFrame(purchases)
    result = df[df.price >= min_price]
    return result.to_dict(orient='records')

def average_price_by_category(purchases):
    df = pd.DataFrame(purchases)
    result = df.groupby('category')['price'].mean().to_dict()
    return result

def most_frequent_category(purchases):
    df = pd.DataFrame(purchases)
    result = df.groupby('category')['quantity'].sum()
    return result.idxmax()

a = total_revenue(purchases)
b = items_by_category(purchases)
c = expensive_purchases(purchases, 1)
d = average_price_by_category(purchases)
e = most_frequent_category(purchases)


print(f'Общая выручка: {a}')
print(f'Товары по категориям: {b}')
print(f'Покупки дороже {1}: {c}')
print(f'Средняя цена по категориям: {d}')
print(f'Категория с наибольшим количеством проданных товаров: {e}')