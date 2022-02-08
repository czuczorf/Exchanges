# Exchanges
Simple exchange management

# Current features
- Gets all of the available exchanges
- Gets the latest price info of a selected product by id on a given exchange

# Database files

For demo purposes the exchange, product and price datas are stored in json files in the [DB directory](https://github.com/czuczorf/Exchanges/tree/main/DB). 

# How to use

Define the full path to the database file in the **data_file** variable
```
data_file = "./DB/exchanges.json"
```

To get the list of the exchanges, create an instance of the **ExchangeList** class and use the *exchanges_get()* function.

```
exchanges = ExchangeList(data_file)

for exchange in exchanges.exchanges_get():
    print(f'- {exchange}')
```

To get the price on a specified exchange first you have to create an instance of the **Exchange** class and as parameters use the exchange id and the data file
```
binance = Exchange('binance',data_file)
```

After that you can get the price by using the **price_get()** function with the id of the product
```
binance.price_get('btc')
```

# Output

![Output](https://github.com/czuczorf/Exchanges/blob/main/images/output.jpg)

**For more details, please see the sample** [script](https://github.com/czuczorf/Exchanges/blob/main/Exchange-sample.py)

