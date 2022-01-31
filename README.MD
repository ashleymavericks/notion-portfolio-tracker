# Notion Portfolio Tracker
A python script to automatically update real-time values of stocks and crypto tickers in a Notion Database.

## Features
- Auto update the last price, daily % and value change for NSE tickers in the Notion DB
- Auto update the current price, 1H and 24H % change in price for Cryptocurrencies
- Provides visual indicators for Profit/Loss & Price Change
- Page icons get auto-populated with Crypto project logo
- Provides auto-populated Screener URL for the NSE tickers

## Requirements

```bash
pip3 install requests nsetools
```

## API's Usage:

[Coinlore Cryptocurrency Data API](https://www.coinlore.com/cryptocurrency-data-api)

[Crypto Icons API](https://cryptoicons.org/)

## Automation
Use [Cron](https://crontab.guru) or any scheduler to run the script in the frequency you want, preferred time period is 30 min or 1 hr

### For 30 mins

```
30 * * * * /usr/bin/python3 /home/.../main.py
```
### For 1 hr
```
0 * * * * /usr/bin/python3 /home/.../main.py
```