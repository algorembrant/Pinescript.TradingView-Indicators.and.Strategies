//@version=5
indicator("8PM–9PM Session Range Box (Asia/Manila)", overlay=true, max_boxes_count=500, max_lines_count=500)

//──────────────────────────────
// SETTINGS
//──────────────────────────────
tz = "Asia/Manila"
startHour = 20  // 8:00 PM
endHour   = 21  // 9:00 PM

//──────────────────────────────
// DETECT 8–9PM SESSION
//──────────────────────────────
barTime  = time(timeframe.period, tz)
barHour  = hour(time, tz)
barMin   = minute(time, tz)

inSession = barHour >= startHour and barHour < endHour
sessionStart = barHour == startHour and barMin == 0
sessionEnd   = barHour == endHour and barMin == 0

//──────────────────────────────
// TRACK HIGHS/LOWS DURING SESSION
//──────────────────────────────
var float sessionHigh = na
var float sessionLow  = na
var int   sessionStartIndex = na
var int   sessionEndIndex   = na
var box   sessionBox = na

if sessionStart
    sessionHigh := high
    sessionLow  := low
    sessionStartIndex := bar_index
    sessionEndIndex := na

if inSession
    sessionHigh := math.max(sessionHigh, high)
    sessionLow  := math.min(sessionLow, low)

if sessionEnd and not na(sessionHigh)
    sessionEndIndex := bar_index
    
    // Draw rectangle (box)
    if not na(sessionBox)
        box.delete(sessionBox)
    sessionBox := box.new( left = sessionStartIndex, right = sessionEndIndex, top = sessionHigh, bottom = sessionLow, bgcolor = color.new(color.yellow, 80),border_color = color.new(color.yellow, 0))

    // Draw vertical lines for visual clarity
    line.new(sessionStartIndex, sessionHigh, sessionStartIndex, sessionLow, color=color.new(color.yellow, 0))
    line.new(sessionEndIndex, sessionHigh, sessionEndIndex, sessionLow, color=color.new(color.yellow, 0))
