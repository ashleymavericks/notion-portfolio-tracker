# Notion Portfolio Tracker
A python script to automatically update real-time values of stocks and crypto tickers in a Notion Database.

## Features:
- Auto update the last price, daily % and value change for NSE tickers in the Notion DB
- Provides auto-populated [Screener](https://screener.in) URL for NSE tickers and [CoinMarketCap](https://coinmarketcap.com) URL for Cryptos
- Auto update the current price, 1 hr, 24 hr and 7 day % change in price for Crypto Coins
- Provides visual indicators for Profit/Loss & Price Change
- Page icons get auto-populated with respective Crypto project logo

## Requirements:

```bash
pip3 install requests nsetools
```

## API's Usage:

[Coinlore Cryptocurrency Data API](https://www.coinlore.com/cryptocurrency-data-api)

[Crypto Icons API](https://cryptoicons.org/)

[Notion Official API](https://developers.notion.com/reference/intro)

## Script Automation:
Use [Cron](https://crontab.guru) or any scheduler to run the script in the frequency you want, preferred time period is 30 min or 1 hr

### For 30 mins

```
30 * * * * /usr/bin/python3 /home/.../main.py
```
### For 1 hr
```
0 * * * * /usr/bin/python3 /home/.../main.py
```