## Pine Script ≠ JavaScript

Files are named with a **`.js`** extension purely for aesthetics. This **does not affect functionality**.

## Why?

GitHub doesn’t support Pine Script, the language for TradingView indicators and strategies. Using `.js` allows GitHub to recognize a language for repository stats. Syntax highlighting is available via VS Code packages, but the code **only works when pasted into TradingView’s Pine Editor**.


## How to use the code

Each project has two main files:

1. **`CODE_notice.file`** – Contains full project details and features. Read this first.  
2. **`CODE_framework.file`** – The Pine Script code to paste into Pine Editor. Focus on this file for implementation.


## Other significant files

Pine Script cannot automate trades inside a broker. For automation, the Pine Script logic is translated into **Python**, optimized for fully automated trading with a broker.

The bot trades **without human interaction**—no chart watching, no emotions, just automated execution.

---

# Indicator Lists

| CODE | Info | Status | Details |
|------|------|--------|---------|
| **[89RS-indi](./Pinescript%20Language/Indicators/89RS.Rangebreakout-Stoporder)** | The 8-9pm Rangebreakout Stoporder Method with 1:2RR ratio target. An Opening Range Break (ORB) reference. | Ongoing | **[readme](https://github.com/algorembrant/Pinescript.TradingView-Indicators.and.Strategies/blob/main/Pinescript%20Language/Indicators/89RS.Rangebreakout-Stoporder/89RS-indi.notice.md)** |


# Strategy Lists

| CODE | Info | Status | Details |
|------|------|--------|---------|
| **[89RS-stra](https://github.com/algorembrant/Pinescript.TradingView-Indicators.and.Strategies/tree/main/Pinescript%20Language/Strategies)** | Automated strategy trading bot for 89RS | Ongoing | **[readme](https://github.com/algorembrant/Pinescript.TradingView-Indicators.and.Strategies/blob/main/Pinescript%20Language/Strategies/89RS-stra.%20Automated%20Trading/89RS-stra.notice.%20Automated%20strategy.md)** |  


# Technique Lists

| CODE | Info | Status | Details |
|------|------|--------|---------|
| **[30WE](https://github.com/algorembrant/Pinescript.TradingView-Indicators.and.Strategies/tree/main/Pinescript%20Language/Techniques)** | The three 30-minute candle wickyoff pattern as entry model to have tighter stoploss to increase the R-multiple | Finished | **[readme](https://github.com/algorembrant/Pinescript.TradingView-Indicators.and.Strategies/blob/main/Pinescript%20Language/Techniques/330WEM.%20three-30minuteWickyoff.EntryModel/30%20minute%20wickyoff%20swingpoint%20entry%20model.md)** |
