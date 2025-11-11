//@version=5
indicator("8PM–9PM Candle Coordinate Finder (Asia/Manila)", overlay=true, max_labels_count=500)

// ─── SETTINGS ───
tz = "Asia/Manila"
startHour = 20  // 8:00 PM
endHour   = 21  // 9:00 PM

// ─── DETECT CANDLES IN THE 8PM–9PM RANGE ───
t = timenow
bar_time = time(timeframe.period, tz)
bar_hour = hour(time, tz)

isInRange = bar_hour >= startHour and bar_hour < endHour

// ─── WHEN A CANDLE FALLS IN THE RANGE ───
if isInRange
    var color c = color.new(color.yellow, 0)
    // Draw box for the 8PM–9PM candle
    box.new(left=bar_index, top=high, right=bar_index + 1, bottom=low, border_color=color.new(color.yellow, 0),bgcolor=color.new(color.yellow, 90) )

    // Label with coordinates
    label.new( bar_index, high, str.format("x: {0}\ny: {1}", str.tostring(bar_index), str.tostring(high)), style=label.style_label_down,  color=color.new(c, 0), textcolor=color.black, size=size.small)

// ─── OPTIONAL: SHOW SESSION LINE ───
if (bar_hour == startHour) and (minute(time, tz) == 0)
    line.new(bar_index, high, bar_index, low, color=color.new(color.orange, 0), style=line.style_dotted)
