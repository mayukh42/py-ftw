# Zeller's Congruence

days = {0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday'
}

dm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def zeller(m, d, y, c):
    if m < 3:
        m += 10
        y -= 1
    else:
        m -= 2
    z = (13*m - 1)/5 + y/4 + c/4 + d + y - 2*c
    return days[z % 7]

def isDateValid(m, d, y, c):
    if m == 2:
        if (y == 0 and c % 4 == 0) or (y > 0 and y % 4 == 0):
            return d in range(1, dm[1]+2) # leap year
        else:
            return d in range(1, dm[1]+1)
    elif m in range(1, 13) and d in range(1, dm[m-1]+1):
        return True
    else:
        return False


def main():
    m = raw_input("Enter month [1-12]: ")
    d = raw_input("Enter day [1-31]: ")
    y = raw_input("Enter year (yyyy)")
    # m = 10
    # d = 27
    # y = 1900
    c = y/100
    y -= c*100
    if isDateValid(m, d, y, c):
        print 'The day of week on', str(m), '/', str(d), '/', str(c*100 + y), 'is', zeller(m, d, y, c)
    else:
        print 'Invalid date'


if __name__ == '__main__':
    main()
