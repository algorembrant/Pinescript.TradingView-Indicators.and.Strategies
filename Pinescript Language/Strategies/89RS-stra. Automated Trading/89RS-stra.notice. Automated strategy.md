Now that we successfully made the framework of the setup to trade, we will clarify conditions to meet for the pinescript trading strategy.

0.  Use asianmanila timezone, UTC+8.
1.  Identify the 8pm to 9pm range.
2.  The processing candles outside the range will become leading factor for trading decision.
3.  The developing price (with wick data) must revisit the mid-price of the range before proceeding to the next condition.
4.  If it visits the mid-price, then make a buystop at the high-price and sellstop at the low-price of the range.
5.  TP price with a target of 2R-multiple.
6.  SL price is at the mid-price for both buystop and sellstop.
7.  The strategy may trigger both buystop and sellstop at the same one setup but the condition is valid until the 4am candle.
8.  Thats how an intraday trading will be finish, maximum of 2 losses or 2 wins or mix or both for range setup.
9.  If the trade is running, and doesn't hit any posible outcome, then take out the order if the price hits 4am.
The starting capital is $2000.
The risk% (of updated capital) is 3% pertrade (3% for buystop and 3% for sell stop).

Use the y-coordinates from my indicator to find range, entries, sl, and tp targets.

![image](https://github.com/algorembrant/Pinescript.TradingView-Indicators.and.Strategies/Pinescript Language/Strategies/images/Screenshot 2025-11-12 201257.png)

| About Flaws            | Details                                    | Status
|---------------------|-------------------------------------------|-------------|
| **Position sizing** | i think the bot doesn't position size condifering the P&L gains. For example: it bets 3% but not as the whole SL, hence the loss is greater than -3% and the gain is greater than 6% | unfixed |
