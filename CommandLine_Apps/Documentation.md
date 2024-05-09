# CommandLine Apps
The command-line application simplifies stock analysis and portfolio management for users of all skill levels.

## App Usage
(very simple to use: users can get all stock analysis, portfolio management, and even time series forcasting by simply choosing Y/N (yes or no), stock tickers, date range, and model names) <br />

**MyApp Workflow for users Example**
```
"Do you want to check sp500 companies tickers (Y/N)?"   ---(Y or N)
```
```
"Type Y to retrieve today benchmark stock prices, type N to customize your own stock price retrieval):"    ---(Y or N)

"Type single/multiple stock tickers you want to retrieve:"   ---(stock tickers)

"Type start date you want to enquire (if only want to price of today, type T):"     ---(start date or T)

"Type end date you want to enquire:"    ---(end start)
```
$\textcolor{red}{(automatically\ scrape\ stock\ prices\ and\ calculate\ stock\ simple\ and\ log\ returns)}$

```
"Do you want to check descriptive statistics for all stock returns?(Y/N)"    ---(Y or N)
"Do you want to show stock plots? (Y/N)"    ---(Y or N)
"Please type window size (integer) for moving average and volatility:"    ---(int days)
```
```
"Do you want to check regression plots (Y/N)?"   ---(Y or N)
```
```
"Do you want to make a portfolio or not (Y/N)?"    ---(Y or N)
"Do you want to use the above simple returns to make your portfolio? (Y/N)"    ---(Y or N)
"Type your own stock tickers to make a new portfolio:"    ---(stock tickers)
"Which year do you want to use to make your portfolio?"   ---(int year)
```
$\textcolor{red}{(automatically\ get\ maximum\ sharpe\ ratio\ portfolio\, \ minimum\ volatility\ portfolio\ and\ all\ portfolios\ table)}$
```
"Do you want to get financial indicators (Y/N)?"    ---(Y or N)
```
$\textcolor{red}{(all\ stock\ tickers\ and\ stock\ date\ range\ input)}$

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
  1. *<ins>reg_plot:</ins>* <br />
     Regression relationship between all selected stock returns and our benchmarks'. <br />

     ![aapl_reg](https://github.com/YuruJing/FinTech/assets/96546138/b7639a02-d3cc-4800-8fd3-97fae3ee0b02)
     
     ![msft_reg](https://github.com/YuruJing/FinTech/assets/96546138/5032c48b-12cb-4f45-8bff-fdbb99c5ec45)

- **<ins>portfolio:</ins>** (Make portfolios automatically with the assets user chose)
  1. *<ins>portf_rtn:</ins>* <br />
     Calculate the return of the portfolio
  2. *<ins>portf_vol:</ins>* <br />
     Calculate the volatility of the portfolio
  3. *<ins>mk_portfs:</ins>* <br />
     Create the efficient frontier for the portfolio and returns all portfolios' table. <br />

     ![efficient_frontier](https://github.com/YuruJing/FinTech/assets/96546138/9daa7c13-332d-474e-ae20-d7da5965500c)
     
     The optimal portfolios for selected assets: (greatest return or lowest risk) <br />

     ![portfolio_results](https://github.com/YuruJing/FinTech/assets/96546138/4c6bdfcb-c580-4007-962b-013a53a4c9a6)

- **<ins>finance_indicators:</ins>** (Calculate the most important financial indicators and extract final features for future time series forcasting.) <br />
  1. *<ins>MAV:</ins>* <br />
     Calculate the moving average and volatility of the adjusted close prices.
  2. *<ins>RSI:</ins>* <br />
     Calculate the relative strength index of the adjusted close prices. 
  3. *<ins>MACD:</ins>* <br />
     Calculate the moving average convergence divergence of the adjusted close prices.
  4. *<ins>extract_features:</ins>* <br />
     Combine all the significant financial indicators with original scraping (open, close, adjusted close, high, low, volume) and returns. <br />
     
     ![features_extract](https://github.com/YuruJing/FinTech/assets/96546138/33941bcc-c7de-4f7e-8697-256c4b527a6e)
     
- **<ins>models:</ins>** (general dataloaders with slices of features and forcasting models for time series forcasting). <br />
  1. *<ins>LSTM:</ins>* <br/> The Deep Learning model for time series forcasting.
 
## Future Improvements and Potential Bugs


     


