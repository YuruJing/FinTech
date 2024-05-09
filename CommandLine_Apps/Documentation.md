# CommandLine Apps
The command-line application simplifies stock analysis and portfolio management for users of all skill levels.


## Modules
- **<ins>get_stocks:</ins>**
  1. *<ins>get_stock_tickers:</ins>* (automatically scrape sp500 companies stock tickers in Wiki)
     
     ![sp500](https://github.com/YuruJing/FinTech/assets/96546138/974791d9-1392-482e-abbe-98bc877e7625)
  2. *<ins>get_stock_price:</ins>* <br />
      Scrape stock prices directly from [Yahoo Finance](https://uk.finance.yahoo.com/) <br />
  
      Choose <ins>defualt mode</ins> to scrape today's stock prices for our makert benchmarks 'SPY', 'BND', 'GLD', 'QQQ', 'VTI'. <br />
      
      Choose <ins>customized mode</ins> to scrape today or customized date range stock prices. <br />
     
     ![scrape_price](https://github.com/YuruJing/FinTech/assets/96546138/8263a9d8-1703-4bd4-9d0d-5f88da4dbf32)

  3. *<ins>stock_rtns:</ins>* <br />
      Simple and log returns will be calculated for stock price inputs. <br />
      
      ![return_df](https://github.com/YuruJing/FinTech/assets/96546138/be20731d-fa46-4596-920b-fb1555c388fd)

     Calculate the descriptive statistics for stock returns (if the user chooses Y). <br />
     
     ![return_print](https://github.com/YuruJing/FinTech/assets/96546138/aac82abd-8be1-4d1c-a63a-548b75866e5c)

     Plotting stock returns and stock moving average of returns (if the user choose Y and set their own moving days window). <br />
     
     ![stock_return2](https://github.com/YuruJing/FinTech/assets/96546138/24d9a3db-9add-41cb-923b-06b09a1846a5)
     
     ![stock_returns](https://github.com/YuruJing/FinTech/assets/96546138/a4a017f7-7411-4598-98ee-e4c2c1a15995)

- **<ins>plotting:</ins>**



