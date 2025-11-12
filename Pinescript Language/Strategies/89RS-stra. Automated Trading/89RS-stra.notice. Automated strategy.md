# 8PM–9PM Range Breakout Trading Strategy (Pine Script)

**Setup Overview:**  
This framework defines the conditions for executing the trading strategy.

---

## Rules

1. Use **Asia/Manila timezone (UTC+8)**.  
2. Identify the **8 PM – 9 PM price range**.  
3. Candles outside this range will guide trading decisions.  
4. The developing price (including wicks) **must revisit the mid-price** of the range before proceeding.  
5. Once the mid-price is revisited:  
   - Place a **Buy Stop** at the range **high**.  
   - Place a **Sell Stop** at the range **low**.  
6. **Take Profit (TP):** 2R multiple from the entry.  
7. **Stop Loss (SL):** mid-price for both Buy Stop and Sell Stop.  
8. Both Buy Stop and Sell Stop **may trigger** in the same setup, valid until the **4 AM candle**.  
9. Maximum outcomes per setup: **2 wins, 2 losses, or a mix**.  
10. If the trade hasn’t hit any target by 4 AM, **cancel the orders**.  

---

## Risk Management

- Starting capital: **$2,000**  
- Risk per trade: **3% of current capital** (applies separately to Buy Stop and Sell Stop).  

---

## Implementation Note

Use the **y-coordinates from the indicator** to calculate the range, entries, SL, and TP targets.

![image](https://github.com/algorembrant/Pinescript.TradingView-Indicators.and.Strategies/blob/main/Pinescript%20Language/Strategies/images/Screenshot%202025-11-12%20201257.png)

---

## Test 1: Result

![image](https://github.com/algorembrant/Pinescript.TradingView-Indicators.and.Strategies/blob/main/Pinescript%20Language/Strategies/images/Screenshot%202025-11-12%20205738.png)

---

## Test 1: Notice 
| Topic&Flaws            | Details                                    | Status  |
|---------------------|-------------------------------------------|-------------|
| **Position sizing** | i think the bot doesn't position size condifering the P&L gains. For example: it bets 3% but not as the whole SL, hence the loss is greater than -3% and the gain is greater than 6% | unresolved |
 |**R-multiple** | its appears that its possible to get 4R-multiple upon reviwing the trades| unresolved |
 |**winrate** | the winrate is 40-43% and its not that idieal|unresolved |

This strategy is naturally profitable but i would like to increase the R-multiples and the winrate, ima run diferrent tests.
