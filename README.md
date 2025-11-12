# Pinescript ≠ Javascript 
I will be using ".js" (JavaScript) in naming a file/s only for aesthetic-look of the code and has nothing to do with the function. 

**Why?** 

GitHub doesn't support Pinescript (a language for making trading indicators and automated strategies). However, the nearest language simillar to pinescript is javascript. That way the system will count it as element language for statistics (% about how often a language is used inside the repository). 

Altho it doesn't suport pinescript function, there's a package for the colored syntax in VS. The output (visualization indicators and strategies) doesn't show up unless we paste the pinescript code on it's intended IDE, which is the PineEditor in the TradingView platform.  


**How to use the code?**

There's 2 significat files for every project. First is the "CODE_**notice**.file", I highly suggest reading this in the begining cuz this is where the *detailes and feature* of the project is all about. Second is the "CODE_**framework**.file", I highly suggest focusing on this oneshot pinescript code cuz this is meant to be pasted on PineEditor in the TradingView platform.


**What is the other significant files?**

The indicators & strategies (pinescript) at TradingView is limited, it doesn't automate trades. Hence, a Phython code is preffered to use for automation. These pinescript code is translalted and optimized to match the desired strategy and be able to automate the trades and operates inside a broker. Trading using a bot, no human interaction/decision making, no looking at the chart, no emotion, just automated trader.


# Indicator Lists

| CODE             | Info                                    | Status    | Details|
|---------------------|-------------------------------------------|-----------------|--|
| **[89RS-indi](./Pinescript%20Language/Indicators/89RS.Rangebreakout-Stoporder)** |The 8-9pm Rangebreakout Stoporder Method with 1:2RR ratio target. An Opening Range Break (ORB) reference. |  Ongoing | **[readme](https://github.com/algorembrant/Pinescript.TradingView-Indicators.and.Strategies/blob/main/Pinescript%20Language/Indicators/89RS.Rangebreakout-Stoporder/89RS-indi.notice.md)** |

# Strategy Lists

| CODE             | Details                                    | Status    |
|---------------------|-------------------------------------------|-----------------|
| **[89RS-stra](https://github.com/algorembrant/Pinescript.TradingView-Indicators.and.Strategies/tree/main/Pinescript%20Language/Strategies)** |Automated strategy trading bot for 89RS |  Ongoing | **[readme](https://github.com/algorembrant/Pinescript.TradingView-Indicators.and.Strategies/blob/main/Pinescript%20Language/Indicators/89RS.Rangebreakout-Stoporder/89RS-indi.notice.md)** |
| **[89RS-stra](https://github.com/algorembrant/Pinescript.TradingView-Indicators.and.Strategies/tree/main/Pinescript%20Language/Strategies)** |Automated strategy trading bot for 89RS |  Ongoing | **[readme]()** |


# Technique Lists

| CODE             | Details                                    | Status    |
|---------------------|-------------------------------------------|-----------------|
| **[30WE](https://github.com/algorembrant/Pinescript.TradingView-Indicators.and.Strategies/tree/main/Pinescript%20Language/Techniques)** | The three 30minute candle wickyoff pattern as entry model to have tigher stoploss to increase the R-multiple| Finished | 
