import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow

# Example values (replace with real candle data)
range_low = 1975
range_high = 1985
range_mid = (range_high + range_low) / 2

# Calculate Buy/Sell Stop and TP levels
buy_stop = range_high
sell_stop = range_low
sl_level = range_mid
tp_buy = buy_stop + 2 * (buy_stop - sl_level)
tp_sell = sell_stop - 2 * (sl_level - sell_stop)

# Create figure
fig, ax = plt.subplots(figsize=(6, 10))

# Draw the 8PM–9PM candle range rectangle
range_rect = Rectangle((0.4, range_low), 0.2, range_high - range_low, color='lightblue', alpha=0.5)
ax.add_patch(range_rect)
ax.text(0.61, (range_low+range_high)/2, '8PM–9PM candles', rotation=90, va='center', fontsize=10)

# High, Mid, Low horizontal lines
ax.hlines(range_high, 0.35, 0.65, color='green', linewidth=2, label='High / Buy Stop')
ax.hlines(range_mid, 0.35, 0.65, color='orange', linewidth=2, label='Mid / SL')
ax.hlines(range_low, 0.35, 0.65, color='red', linewidth=2, label='Low / Sell Stop')

# TP levels
ax.hlines(tp_buy, 0.2, 0.8, color='darkgreen', linestyle='--', linewidth=1.5, label='Buy TP')
ax.hlines(tp_sell, 0.2, 0.8, color='darkred', linestyle='--', linewidth=1.5, label='Sell TP')

# Add Buy/Sell arrows
ax.add_patch(FancyArrow(0.7, range_mid, 0.2, buy_stop - range_mid, width=0.01, color='green', label='Buy Stop'))
ax.add_patch(FancyArrow(0.7, range_mid, 0.2, sell_stop - range_mid, width=0.01, color='red', label='Sell Stop'))

# Add labels for levels
ax.text(0.66, range_high, f'High\n{buy_stop}', color='green', fontsize=10)
ax.text(0.66, range_mid, f'Mid\n{sl_level}', color='orange', fontsize=10)
ax.text(0.66, range_low, f'Low\n{sell_stop}', color='red', fontsize=10)
ax.text(0.66, tp_buy, f'TP Buy\n{tp_buy}', color='darkgreen', fontsize=10)
ax.text(0.66, tp_sell, f'TP Sell\n{tp_sell}', color='darkred', fontsize=10)

# Cosmetic settings
ax.set_xlim(0, 1.2)
ax.set_ylim(range_low - 10, tp_buy + 10)
ax.set_xticks([])
ax.set_ylabel('Price')
ax.set_title('XAUUSD 8PM–9PM Range Breakout Setup', fontsize=14, pad=20)
ax.legend(loc='upper left')

plt.show()
