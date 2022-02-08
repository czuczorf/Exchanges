import json

class ExchangeList:

    def __init__(self, data_file):
        """
        :param data_file: file name and complete path to exchange file
        """  
        self.exchange_data = json.load( open(data_file) ) 

    def exchanges_get(self):
        return self.exchange_data

class Exchange:

    def __init__(self, exchange_type, data_file):
        """
        :param exchange_type: id of the exchange
        :param data_file: file name and complete path to exchange file
        """  
        self.exchange_type = exchange_type
        self.exchange_data = json.load( open(data_file) ) 
        self.price_data = json.load( open(f'./DB/prices-{exchange_type}.json') )

        self.exchange = self.process_data()

        if(self.exchange==None):
            raise Exception("Exchange not found!")
            return

        self.id = self.exchange["id"]
        self.name = self.exchange["name"]
        self.version = self.exchange["version"]
        self.products = self.exchange["products"]
        self.has_fetch_prices = self.exchange["has"]["fetchPrices"]

    def process_data(self):        
        for key in self.exchange_data:
            if self.exchange_data[key]["id"]==self.exchange_type:
                return self.exchange_data[key]

    def __str__(self):        
        return f"Exchange : {self.name} " 

    def price_get(self, product):
        """
        :param product: product id
        """          
        if (product not in self.price_data):
            raise Exception("Product not found!")
            return
        else:
            return self.price_data[product]
