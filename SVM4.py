import pandas as pd
import os
import quandl as quandl
import time

# auth_tok = open('auth.txt','r').read()
# data = quandl.get('WIKI/HOV',start_date = '2000-12-12',end_date = '2015-12-12',api_key='mkY--sFmaMDJ1r9Pvmb7')
# print(auth_tok)
# print(data)

path = '/home/sud/workspace/intraQuarter'

def stock_prices():
    df = pd.DataFrame()

    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]

    print(stock_list)
    for each_dir in stock_list[1:]:
        try:
#             each_file = os.listdir(each_dir)
            ticker = each_dir.split("/")[-1]
            name = "WIKI/"+ticker.upper()
            print(name)
            data = quandl.get(name,
                              start_date = "2000-12-12",
                              end_date = "2014-12-30",
                              api_key='mkY--sFmaMDJ1r9Pvmb7')
            data[ticker.upper()] = data["Adj. Close"]
            df = pd.concat([df, data[ticker.upper()]], axis = 1)
        except Exception as e:
            print(str(e))
    df.to_csv('stock_prices.csv')
    
stock_prices()    