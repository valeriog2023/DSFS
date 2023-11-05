# Data classes have ben introduced in python 3.7
# they are normal python classes (not compact as named tuples)
# but they provide some benefits
# basically you add a decorator to an object class
import datetime
from dataclasses import dataclass
from dataclasses import fields as get_dataclass_fields
from typing import List,Optional,Dict, NamedTuple
import re
from dateutil.parser import parse
import csv
from collections import defaultdict,namedtuple

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


##############################
# CLEANING DATA
##############################
def parse_row(row: List[str], verbose:bool=False)-> Optional[StockPrice2]:
    """
    Given as input: row as a list of strings
    this function creates an instance of StockPrice2
    matching the following elements in the list
     row[0]: Symbol<str>
     row[1]: date<datetime>
     row[2]: <closing_price<float>
    """
    symbol, date_, closing_price_ = row
    #
    # stock symbol should be all capital letter
    if not re.match(f"^[A-Z]+$", symbol):
        return None
    #
    try:
        date = parse(date_).date()
    except ValueError:
        if verbose: print(f"Error Coverting date {date_} Error is {ValueError}")
        return None
    #
    try:
        closing_price = float(closing_price_)
    except ValueError:
        if verbose: print(f"Error Coverting closing_price {closing_price_} Error is {ValueError}")
        return None
    #
    return StockPrice2(symbol=symbol,
                       date= date,
                       closing_price=closing_price)


assert parse_row(["MSFT0","6/20/2014","41.68"]) is None
assert parse_row(["MSFt","6/20/2014","41.68"]) is None
assert parse_row(["MSFT","6-20--2014","41.68"]) is None
assert parse_row(["MSFT0","6/20/2014","x"]) is None

test_file="data_files/comma_delimited_stockprice.csv"
data:List[StockPrice2] = []
with open(test_file,'r') as f:
    reader = csv.reader(f)
    for row in reader:
        stock = parse_row(row)
        if stock is None:
            print(f"Skipping row: {row}")
        else:
            data.append(stock)
# File content is and
#AAPL,6/20/2014,90.91
#MSFT,6/20/2014,41.68
#FB,6/20/3014,64.5
#AAPL,6/19/2014,91.86
#MSFT,6/19/2014,n/a
#FB,6/19/2014,64.34
#[..]
#
# we define a default Dict, if we have no value we return the result from lambda: -infinite
max_prices: Dict[str, float] =  defaultdict(lambda: float('-inf'))

for sp in data:
    symbol,closing_price = sp.symbol,sp.closing_price
    if closing_price > max_prices[symbol]:
        max_prices[symbol] = closing_price
#
# let's now look for the stock with major price changes
prices:Dict[str, List[StockPrice2]] = defaultdict(list)
#
# we create a dict where key is the symbol and value is the list of stock prices
for sp in data:
    prices[sp.symbol].append(sp)
#
# now order prices by date
prices = { symbol: sorted(values, key =lambda x: x.date)
                          for symbol,values in prices.items() }
#
#
def pct_change(yesterday:StockPrice2,today:StockPrice2)->float:
    """Returns the prcentage of change between yesterday and today price as float
       note the formula is
       ((price_today - price_yesterday) / price_yesterday) * 100
       but we can also write it in the form
       ((price_today/price_yesterday) - (price_yesterday/price_yesterday)) * 100
       which is
       ((price_today/price_yesterday) - 1) * 100
    """
    return ((today.closing_price/yesterday.closing_price) -1 ) * 100

class DailyChange(NamedTuple):
    symbol: str
    date: datetime.date
    pct_change: float


def day_over_day_changes(prices:List[StockPrice2]) -> List[DailyChange]:
    """
    Gets as input the list of stockprices for a symbol
    and returns a list of tuples with the daily changes
    """
    return [DailyChange(symbol=today.symbol,
                        date=today.date,
                        pct_change=pct_change(today,yesterday)
                        )
            for today,yesterday in zip(prices,prices[1:]) # this puts together prices with itself
                                                          # and generates a list of tuples of size N-1
                                                          # e.g. from the list [1,2,3,4]
                                                          # it will generate [(1,2),(2,3),(3,4)]
            ]

all_changes = [ change
               for symbol_values in prices.values()
               for change in day_over_day_changes(symbol_values)]

#
# at this point we can easily find the max and min changes
print("All changes are:")
import pprint
pprint.pprint(all_changes)
print("======\nNow it's easy to find max and mi of all changes")
max_change = max(all_changes, key=lambda x: x.pct_change)
min_change = min(all_changes, key=lambda x: x.pct_change)
print(f"Max change is for: {max_change}")
print(f"Min change is for: {min_change}")

