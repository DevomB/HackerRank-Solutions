def timeConversion(s):
    time, meridiem = s[:-2], s[-2:] 
    # Get the full time and the  meridiem indicator (AM/PM)
    hours, minutes_seconds = time[:2], time[2:] 
    # split the string into hours and minutes/seconds

    if meridiem == "AM":
        hours = "00" if hours == "12" else hours
    else:
        if hours != "12":
            hours = str(int(hours) + 12)

    return hours + minutes_seconds