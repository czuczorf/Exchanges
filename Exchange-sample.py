import datetime
from Exchange import Exchange, ExchangeList

data_file = "./DB/exchanges.json"

# ----------------------------------------
#  List of available exchanges
# ----------------------------------------

exchanges = ExchangeList(data_file)

print("List of exchanges:")
for exchange in exchanges.exchanges_get():
    print(f'- {exchange}')

# ----------------------------------------
#  BINANCE Exchange
# ----------------------------------------

binance = Exchange('binance',data_file)

# Info 

print(f'\nExchange : {binance.name}, Id : {binance.id}, Version : {binance.version}, Supports fetch prices? : {binance.has_fetch_prices}\n')

# Products and the closing price

for product in binance.products:
    product_id = binance.products[product]["id"]
    price = binance.price_get(product_id)
    date = datetime.datetime.fromtimestamp( price["timestamp"])
    print(f'Product : {product}, Closing price : {price["close"]}, Date : {date}')

# ----------------------------------------
#  FTX Exchange
# ----------------------------------------

ftx = Exchange('ftx',data_file)

# Info 

print(f'\nExchange : {ftx.name}, Id : {ftx.id}, Version : {ftx.version}, Supports fetch prices? : {ftx.has_fetch_prices}\n')

# Products and the closing price

for product in ftx.products:
    product_id = ftx.products[product]["id"]
    price = ftx.price_get(product_id)
    date = datetime.datetime.fromtimestamp( price["timestamp"])
    print(f'Product : {product}, Closing price : {price["close"]}, Date : {date}')
