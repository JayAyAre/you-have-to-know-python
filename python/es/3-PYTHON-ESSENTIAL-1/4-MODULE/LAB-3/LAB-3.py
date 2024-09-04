def is_year_leap(year):
    if type(year) == int:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        return None


def days_in_month(year, month):
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    else:
        return 30


def day_of_year(year, month, day):
    if type(day) == int:
        total_days = 0
        for i in range(1, month):
            aux = days_in_month(year, i)
            if aux == None:
                return None
            total_days += days_in_month(year, i)
        return total_days + day
    else:
        return None


test = [[2000, 12, 31], [2000, 2, 29], [2016, 1, 31], [1987, 11, 30]]
expected_results = [366, 60, 31, 334]
for i, date in enumerate(test):
    print(day_of_year(date[0], date[1], date[2]), "-> ", end="")
    if day_of_year(date[0], date[1], date[2]) == expected_results[i]:
        print("OK")
    else:
        print("Failed")
