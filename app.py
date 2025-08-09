import pandas as pd
from sklearn.linear_model import LinearRegression
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
df = pd.read_csv('dataset/house_prices.csv')

X = df['size'].values.reshape(-1, 1)
y = df['price'].values

model = LinearRegression()
model.fit(
    X,
    y
)

size = input('Enter with your house size m² that are you looking for: ')

predictions = model.predict([[int(size)]])

print(f"Regression results in price: {locale.currency(predictions[0], grouping=True)}")