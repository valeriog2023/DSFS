import datetime
#
# Dictionaries are not efficient:
#  - they are objects and come with overhead
#  - can type annotate them to get help/hint from editors
# You can however dynamically change them.
# If that's not a main requirement, consider using 
#
#               named_tuples
#
from collections import namedtuple
from typing import NamedTuple

StockPriceBase = namedtuple('StockPrice',['symbol','date','closing_price'])
price = StockPriceBase('MSFT', datetime.datetime(2018,12,14), 106.03)

assert price.symbol == 'MSFT'
assert price.closing_price == 106.03
#
# you can't modify a namedtuple once it's created but it's more efficient for computation
#
# this is how you would annotate it
# define an object as a sub class of NamedTuple 
# note: this is the one that comes from typing
#       not the one that comes from collections
class StockPrice(NamedTuple):
    symbol: str
    date: datetime.datetime
    closing_price: float

    def is_high_tech(self) -> bool:
        """returns a boolean;
        true if  symbol is in a specific list
        """
        return self.symbol in ['MSFT','FB','AMZN','AAPL', 'GOOG']
    

#
# recreating the stock
price = StockPrice('MSFT', datetime.datetime(2018,12,14), 106.03)    
assert price.symbol == 'MSFT'
assert price.closing_price == 106.03
assert price.is_high_tech()

#
# if you use price. you can see the named keys (date, symbol, closing_price etc..)