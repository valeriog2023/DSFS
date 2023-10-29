# Data classes have ben introduced in python 3.7
# they are normal python classes (not compact as named tuples)
# but they provide some benefits
# basically you add a decorator to an object class
import datetime
from dataclasses import dataclass
from dataclasses import fields as get_dataclass_fields

@dataclass
class StockPrice2:
    symbol: str
    date: datetime.datetime
    closing_price: float

    def is_high_tech(self) -> bool:
        """returns a boolean;
        true if  symbol is in a specific list
        """
        return self.symbol in ['MSFT','FB','AMZN','AAPL', 'GOOG']
    
price2 = StockPrice2('MSFT', datetime.datetime(2018,12,14), 106.03)    
assert price2.symbol == 'MSFT'
assert price2.closing_price == 106.03
assert price2.is_high_tech()
#
# the difference compared to before is that you can modify your object
print("Dataclass test")
print(f"Closing price is now: {price2.closing_price}")
price2.closing_price /= 2
print(f"Closing price is now: {price2.closing_price}")
print("Price change would not be possible with named tuples")
print("it also leaves possibility of other errors (same as a normal dict, you can add fields)")
#
# there are a few eay you can see what fields are in a dataclass
# - dataclasses.fields
# or via the inspect library
# import inspect
# inspect.getmembers(type(price2))
fields = get_dataclass_fields(price2)
for f in fields:
    print(f"Key in price2: {f.name}")
print("Now adding a new field by mistake: cosing_price instead of closing_price")
price2.cosing_price = 100
fields = get_dataclass_fields(price2)
for f in fields:
    print(f"Key in price2: {f.name}")
print("It is not recognized as a new field but you can still get the value")
print(f"price2.closing_price {price2.closing_price}")
print(f"price2.cosing_price {price2.cosing_price}")

