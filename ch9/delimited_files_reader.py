import csv
with open('data_files/tab_delimited_stockprice.txt','r') as f:
    tab_reader =  csv.reader(f, delimiter='\t')
    for row in tab_reader:
        date = row[1]
        symbol = row[0]
        try:
            closing_price = float(row[2]) # this will throw an exception for values like 'n/a'
        except:
            closing_price = 'n/a'
        #
        # do something with it
        # :>4 means align right and use standard length of 4 if possible
        print(f"date: {date}, symbol: {symbol:>4}, closing price: {closing_price:>6}")

print("\n\n--------------- Using Dict reader for files with heders")
with open('data_files/stock_price_with_headers.txt','r') as f:
    dict_reader =  csv.DictReader(f, delimiter=':')
    for dict_row in dict_reader:
        symbol = dict_row['Symbol']
        date = dict_row['Date']
        closing_price = dict_row['Closing Price']        
        print(f"date: {date}, symbol: {symbol:>4}, closing price: {closing_price:>6}")

# csv.reader support other delimiter options like delimiter = ':' , delimeter ="," etc..
# if the file has headers like:
# AAPL	6/20/2014	90.91
# MSFT	6/20/2014	41.68
# FB	6/20/3014	64.5
# AAPL	6/19/2014	91.86
# MSFT	6/19/2014	n/a
# FB	6/19/2014	64.34