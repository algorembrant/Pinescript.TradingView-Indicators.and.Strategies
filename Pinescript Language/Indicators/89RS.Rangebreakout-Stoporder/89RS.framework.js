//@version=5
indicator("8PM–9PM Candle High & Low (Asia/Manila)", overlay=true, max_lines_count=500)

// ─────────────────────────────
// SETTINGS
// ─────────────────────────────
timeZone = "Asia/Manila"

// Get the current bar's hour and minute in Manila timezone
barHour   = hour(time, timeZone)
barMinute = minute(time, timeZone)

// ─────────────────────────────
// DETECT 8PM–9PM CANDLE RANGE
// ─────────────────────────────

// Start when hour == 20 (8PM)
isSession = (barHour == 20)

// Reset at 9PM
isReset = (barHour == 21 and barMinute == 0)

// Persistent variables to store the range
var float sessionHigh = na
var float sessionLow  = na

if isSession
    sessionHigh := na(sessionHigh) ? high : math.max(sessionHigh, high)
    sessionLow  := na(sessionLow)  ? low  : math.min(sessionLow, low)
else if isReset
    sessionHigh := na
    sessionLow := na

// ─────────────────────────────
// DRAW LINES FOR THE 8PM–9PM RANGE
// ─────────────────────────────
var line hiLine = na
var line loLine = na

if barstate.islast and not na(sessionHigh) and not na(sessionLow)
    line.delete(hiLine)
    line.delete(loLine)
    hiLine := line.new(bar_index - 1, sessionHigh, bar_index + 10, sessionHigh, extend=extend.right, color=color.new(color.green, 0), style=line.style_dotted)
    loLine := line.new(bar_index - 1, sessionLow, bar_index + 10, sessionLow, extend=extend.right, color=color.new(color.red, 0), style=line.style_dotted)

// ─────────────────────────────
// LABELS
// ─────────────────────────────
if barstate.islast and not na(sessionHigh) and not na(sessionLow)
    label.new(bar_index + 2, sessionHigh, "8PM High", style=label.style_label_down, color=color.new(color.green, 70))
    label.new(bar_index + 2, sessionLow, "8PM Low", style=label.style_label_up, color=color.new(color.red, 70))
