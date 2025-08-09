# House Price Prediction with Linear Regression

This project is a simple implementation of **Linear Regression** to predict house prices based on their size (in square meters).

## Description

- The dataset (`dataset/house_prices.csv`) contains two columns:  
  - `size`: size of the house in square meters  
  - `price`: price of the house in dollars

- We train a linear regression model on this data to learn the relationship between house size and price.

- The user is prompted to input a house size, and the program predicts the expected price using the trained model.

## Requirements

- Python 3.x  
- pandas  
- scikit-learn  

You can install the required packages with:

```bash
pip install pandas scikit-learn

```

## How to Run
Make sure the dataset CSV file is located at dataset/house_prices.csv.

When prompted, enter the size of the house in square meters, for example:

```bash
Enter with your house size m² that are you looking for: [INPUT_VALUE]
```

The program will output the predicted price formatted in USD currency, for example:

```bash
Regression results in price: $350,000.00
```

## Code Explanation
We read the dataset using pandas.

Extract features (size) and labels (price).

Fit a LinearRegression model from scikit-learn.

Use locale to format the output price in US Dollar currency format.

The prediction is made based on user input.