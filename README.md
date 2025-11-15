## Pine Script ≠ JavaScript

Pine Script isn’t like JavaScript because it is a **domain-specific language** designed specifically for **financial charting and trading strategies** on TradingView. Unlike JavaScript, which is a general-purpose language for web development and can manipulate any type of data or interface, Pine Script focuses on **time series data**, **candlestick patterns**, **indicators**, and **strategy execution**.

##  Pinescript versus Python
| Feature/Aspect      | Pine Script                                                                                          | Python                                                                                                     |
| ------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Description**     | Domain-specific language for creating **trading indicators and strategies** on TradingView.          | General-purpose programming language used for **web, data analysis, AI, automation**, and more.            |
| **Primary Use**     | Financial charting, indicators, alerts, backtesting strategies.                                      | Wide range: data analysis, AI/ML, web development, automation, scripting, finance, etc.                    |
| **Execution Model** | Runs **bar by bar** on time series data; series variables track historical values automatically.     | Procedural or object-oriented execution; runs line by line; manual handling of time series required.       |
| **Similarities**    | Both support **functions, variables, loops** (limited in Pine Script), and can perform calculations. |                                                                                                            |
| **Capabilities**    | Specialized plotting, alerts, and strategy execution; handles financial series data efficiently.     | Full programming capabilities including file I/O, networking, libraries (e.g., NumPy, Pandas, Matplotlib). |
| **Limitations**     | Cannot access system files, web APIs, or external libraries; limited to TradingView environment.     | Requires libraries for charting and finance; no built-in trading platform integration.                     |
| **Learning Curve**  | Easier for traders due to focused domain, fewer syntax rules.                                        | Steeper learning curve but more versatile; extensive resources and community support.                      |


##  Fact

GitHub doesn’t support Pine Script, the language for TradingView indicators and strategies. However it's still good for documentation. Syntax highlighting is available via VS Code packages, but the code **only works when pasted into TradingView’s Pine Editor Compiler**.


## How to use the code

Each project is documented.

1. **`CODE.ipynb`** – Contains full project logic, details and features inside a jupyter notebook.  

---

## Indicator & Strategies Lists

| CODE | Info | Status | Details |
|------|------|--------|---------|
| **[89rs](https://github.com/algorembrant/Pinescript.TradingView-Indicators.and.Strategies/blob/main/Trading%20Indicators%2C%20Strategies%20%26%20Techniques/89RM%2089Rangebreakout%20Model.ipynb)** | The 8-9pm Rangebreakout Stoporder Method with 1:2RR ratio target. An Opening Range Break (ORB) reference. | Ongoing |  |

## Concepts Lists

| CODE | Info | Status | Details |
|------|------|--------|---------|
| **[LLN](https://github.com/algorembrant/Pinescript.TradingView-Indicators.and.Strategies/blob/main/Concepts%20and%20Topics/The%20Law%20of%20Large%20Numbers%20(LLN).ipynb)** | The Law of Large Numbers | Finished |  |

## Technique Lists

| CODE | Info | Status | Details |
|------|------|--------|---------|
| **[30WE](https://github.com/algorembrant/Pinescript.TradingView-Indicators.and.Strategies/tree/main/Pinescript%20Language/Techniques)** | The three 30-minute candle wickyoff pattern as entry model to have tighter stoploss to increase the R-multiple | Finished | **[readme](https://github.com/algorembrant/Pinescript.TradingView-Indicators.and.Strategies/blob/main/Pinescript%20Language/Techniques/330WEM.%20three-30minuteWickyoff.EntryModel/30%20minute%20wickyoff%20swingpoint%20entry%20model.md)** |
