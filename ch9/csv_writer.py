import csv
import datetime
today_prices = {'AAPL': 90.91,
                'MSFT': 5.18,
                'FB': 18.23}

date = datetime.date.today()
with open('data_files/csv_write_test1.csv','w') as f:
    csv_writer = csv.writer(f, delimiter=',')
    for stock, price in today_prices.items():
        csv_writer.writerow([stock,price,date])
        print(f"written line: {[stock,price,date]} to data_files/csv_write_test1.csv")

#
# because the actual values have commas inside, you need to be careful
test_with_commas = [[ "test1","success", "Monday" ],
                    [ "test2","success, kind of ", "Tuesday" ],
                    [ "test3","failure, kind of ", "Wednesday" ],
                    [ "test4","failure, utter ", "Thursday" ],
                ]
#
# never write directly to a file (or read), always use reader/writer objects
# because they will manage these scenarios
with open('data_files/csv_write_test2.csv','w') as f:
    csv_writer = csv.writer(f, delimiter=',')
    for line in test_with_commas:
        csv_writer.writerow(line)
        print(f"written line: {line} to data_files/csv_write_test2.csv")
