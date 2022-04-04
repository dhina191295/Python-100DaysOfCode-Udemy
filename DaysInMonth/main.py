def is_leap(year):
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

def days_in_month(year_given,month_given):
    """the month and year given by the user collected and then year is passed to leap year function and if the return value is true, then return 29 days for Feb month, else return the days given in the list for the month value given"""
    if month_given > 12 or month_given < 1:
        return "Invalid Month given"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year_given) and month_given == 2:
        return 29
    return month_days[month_given-1]

#🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
