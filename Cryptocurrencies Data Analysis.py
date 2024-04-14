#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Starting off I import all of the relevant packages required to complete the code
from requests import Session
import json
import pandas as pd
import psycopg2

# Prompt user for input with specifications
input_lst = input("Please enter all cryptocurrencies you would like to view (comma-separated, no spaces (ex. bitcoin,bitcoin cash)): ").lower()

# Change the used input in the required slug format for aquiring information
input_list = input_lst.split(',')
input_list = [name.replace(" ", "-") for name in input_list]

# Creating the empty dataframe to hold the values
df = pd.DataFrame()

# Use code found on CoinMarketCap to access APIs
# Addtionally although I should not usually provide unique API keys I have provided it here for less hassle on your end
for name in input_list:
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    api_key = 'df1709c0-4fb3-4b0c-8d1a-a116e9dbc6b8'
    parameters = {'slug': name, 'convert': 'USD'}
    headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': api_key}

    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    
    # Aquire both the information relevant to each coin and insert it into the dataframe
    # Aquire the crpytocurrency name to save as a variable
    if response.status_code == 200:
        data = response.json()['data']
        crypto_info = data[next(iter(data))]['quote']['USD']
        crypto_name = data[next(iter(data))]['name']
        crypto_info['name'] = crypto_name  # Add 'name' field to the retrieved data
        df = df.append(crypto_info, ignore_index=True)
    # Create an else statement if a coin is not in the valid format or it is spelled incorrectly
    else:
        print(f"Failed to retrieve data for cryptocurrency '{name}'. Please check the spelling and format.")

# Establishing a connection to PostgreSQL
# Enter user specific information here to connect to database created and SQL server used (I have removed my password for privacy purposes)
try:
    conn = psycopg2.connect(
        dbname='CryptoAnalysis',
        user='postgres',
        password='#INSERT PASSWORD HERE',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()

    # Dropping the cryptocurrencies table if it exists
    cursor.execute("DROP TABLE IF EXISTS cryptocurrencies")
    conn.commit()

    # Creating the cryptocurrencies table with specific data types
    cursor.execute("""
        CREATE TABLE cryptocurrencies (
            name TEXT PRIMARY KEY,
            price FLOAT,
            volume_24h FLOAT,
            volume_change_24h FLOAT,
            percent_change_1h FLOAT,
            percent_change_24h FLOAT,
            percent_change_7d FLOAT,
            percent_change_30d FLOAT,
            percent_change_60d FLOAT,
            percent_change_90d FLOAT,
            market_cap FLOAT,
            market_cap_dominance FLOAT,
            fully_diluted_market_cap FLOAT
        )
    """)
    conn.commit()

    # Inserting data into the cryptocurrencies table
    for index, row in df.iterrows():
        cursor.execute("""
            INSERT INTO cryptocurrencies (
                name, price, volume_24h, volume_change_24h, percent_change_1h, percent_change_24h,
                percent_change_7d, percent_change_30d, percent_change_60d, percent_change_90d,
                market_cap, market_cap_dominance, fully_diluted_market_cap
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (name) DO NOTHING
        """, (
            row['name'], row['price'], row['volume_24h'], row['volume_change_24h'],
            row['percent_change_1h'], row['percent_change_24h'], row['percent_change_7d'],
            row['percent_change_30d'], row['percent_change_60d'], row['percent_change_90d'],
            row['market_cap'], row['market_cap_dominance'], row['fully_diluted_market_cap']
        ))
        conn.commit()
        print(f"{row['name']} inserted successfully!")
    
    # Confirming successful data insertion
    print("Data inserted successfully into PostgreSQL!")

# Post an error message if connection is unsuccessful otherwise just close the connection to SQL
except psycopg2.Error as e:
    print(f"Error connecting to PostgreSQL: {e}")
except Exception as e:
    print(f"Error: {e}")
finally:
    if conn is not None:
        conn.close()


# In[ ]:




