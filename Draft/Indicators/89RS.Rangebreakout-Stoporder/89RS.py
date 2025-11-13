import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider
import matplotlib.ticker as mticker

def plot_range(range_low, range_high):
    # Ensure high > low
    if range_high <= range_low:
        print("Error: High must be greater than Low")
        return
    
    range_mid = (range_high + range_low) / 2
    
    # Calculate Buy/Sell Stop and TP levels
    buy_stop = range_high
    sell_stop = range_low
    sl_level = range_mid
    tp_buy = buy_stop + 2 * (buy_stop - sl_level)
    tp_sell = sell_stop - 2 * (sl_level - sell_stop)
    
    # Plot setup
    fig, ax = plt.subplots(figsize=(6, 8))
    
    # Draw 8PM–9PM range rectangle
    ax.fill_betweenx([range_low, range_high], 0.4, 0.6, color='lightblue', alpha=0.5, label='8PM–9PM Range')
    
    # High, Mid, Low lines
    ax.hlines(range_high, 0.3, 0.7, color='green', label='High / Buy Stop')
    ax.hlines(range_mid, 0.3, 0.7, color='orange', label='Mid / SL')
    ax.hlines(range_low, 0.3, 0.7, color='red', label='Low / Sell Stop')
    
    # TP levels
    ax.hlines(tp_buy, 0.2, 0.8, color='darkgreen', linestyle='--', label='Buy TP')
    ax.hlines(tp_sell, 0.2, 0.8, color='darkred', linestyle='--', label='Sell TP')
    
    # Labels for levels
    ax.text(0.65, range_high, f'High\n{buy_stop:.2f}', color='green', fontsize=10)
    ax.text(0.65, range_mid, f'Mid\n{sl_level:.2f}', color='orange', fontsize=10)
    ax.text(0.65, range_low, f'Low\n{sell_stop:.2f}', color='red', fontsize=10)
    ax.text(0.65, tp_buy, f'Buy TP\n{tp_buy:.2f}', color='darkgreen', fontsize=10)
    ax.text(0.65, tp_sell, f'Sell TP\n{tp_sell:.2f}', color='darkred', fontsize=10)
    
    # Cosmetic settings
    ax.set_xlim(0, 1)
    buffer = max(tp_buy - range_low, 10)
    ax.set_ylim(range_low - buffer*0.1, tp_buy + buffer*0.1)
    ax.set_xticks([])
    ax.set_ylabel('Price')
    ax.set_title('XAUUSD 8PM–9PM Range Breakout Setup')
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%.2f'))
    ax.legend(loc='upper left')
    plt.show()

# Interactive sliders
interact(plot_range,
         range_low=FloatSlider(value=1975, min=1900, max=2000, step=0.5, description='Range Low'),
         range_high=FloatSlider(value=1985, min=1900, max=2000, step=0.5, description='Range High'));
