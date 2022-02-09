from curses.ascii import islower
from env_vars import *
import requests
from nsetools import Nse

nse = Nse()
secret_key = NOTION_SECRET_KEY
stocks_database_id = NOTION_STOCKS_DB
crypto_database_id = NOTION_CRYPTO_DB

base_db_url = "https://api.notion.com/v1/databases/"
base_pg_url = "https://api.notion.com/v1/pages/"
base_crypto_url = "https://api.coinlore.net/api/tickers/?start=0&limit=100"

header = {"Authorization": secret_key,
          "Notion-Version": "2021-05-13", "Content-Type": "application/json"}

# Stocks section
response_stocks_db = requests.post(
    base_db_url + stocks_database_id + "/query", headers=header)

for page in response_stocks_db.json()["results"]:
    page_id = page['id']
    props = page['properties']
    asset_code = props['Ticker']['rich_text'][0]['plain_text']
    quote = nse.get_quote(asset_code)
    company_name = quote['companyName']
    checkbox_state = props['Trade Status']['checkbox']
    
    # removing "Limited" | "Ltd" from company name
    company_name = company_name.replace("Limited", "")
    company_name = company_name.replace("Ltd", "")

    stock_price = quote['lastPrice']
    percent_change = float(quote['pChange'])

    if checkbox_state is False:
        data_price = {"properties":
                  {
                      "Current Price": {"number": stock_price},
                      "1D": {"number": percent_change},
                      "Screener URL": {"url": "https://www.screener.in/company/" + asset_code},
                      "Name": {
                          "title": [
                              {"text": {"content": company_name}}
                          ]
                      }
                  }
                  }
        send_price = requests.patch(
            base_pg_url + page_id, headers=header, json=data_price)

# Crypto section
response_crypto_db = requests.post(
    base_db_url + crypto_database_id + "/query", headers=header)

for page in response_crypto_db.json()["results"]:
    page_id = page['id']
    page_icon = page['icon']
    props = page['properties']
    asset_code = props['Ticker']['rich_text'][0]['plain_text']
    request_by_code = requests.get(base_crypto_url).json()['data']
    checkbox_state = props['Trade Status']['checkbox']
    coin = next(
        (item for item in request_by_code if item['symbol'] == asset_code), None)

    if(request_by_code != [] and coin != None):
        price = float(coin['price_usd'])
        percent_1h = float(coin['percent_change_1h'])
        percent_24h = float(coin['percent_change_24h'])
        percent_7days = float(coin['percent_change_7d'])
        rank = int(coin['rank'])
        name = coin['name']
        coin_url = "https://coinmarketcap.com/currencies/" + coin['nameid']

        if checkbox_state is False:
            data_price = {"properties": {
                "Current Price": {"number": price},
                "1H %": {"number": percent_1h},
                "24H %": {"number": percent_24h},
                "7D %": {"number": percent_7days},
                "URL": {"url": coin_url},
                "Rank": {"number": rank},
                "Name": {
                    "title": [
                        {"text": {"content": name}}
                    ]
                }
            }
            }

            send_price = requests.patch(
                base_pg_url + page_id, headers=header, json=data_price)

        # update page icons with the appropriate crypto project logo
        if(page_icon is None):
            payload = {
                "icon": {
                    "type": "external",
                    "external": {
                        "url": "https://cryptoicons.org/api/icon/" + asset_code.lower() + "/200"
                    }
                }
            }
            update_icon = requests.patch(
                base_pg_url + page_id, headers=header, json=payload)