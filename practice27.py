weekdays = ['SUNDAY','MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY']
def dayofweek(month, day, yr):
    centuryAnchor = (16 - 2 * (yr // 100 % 4)) % 7
    yr = yr % 100
    yrs_12 = yr % 12
    offset = yr // 12 + yrs_12 + yrs_12 // 4 + centuryAnchor
    monpos = [0, 3, 0, 7, 4, 9, 6, 11, 8, 12, 10, 14, 12][month]
    if month < 3 and (yr or centuryAnchor == 2) and not yr % 4: 
        monpos += 1
    return weekdays[(35 + day - monpos + offset) % 7]
print(dayofweek(*map(int, input().split())))
