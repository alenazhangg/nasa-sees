""" Creates lists of months and hours to be used as the
x-axis labels and positions for the plots generated. 
"""
import calendar

def monthstohours():
	""" Returns a list of total hours after 2008 that 
	correspond to each month.
	"""
	hrs = []
	startday = 15
	for x in range(1, 13):
		hrs.append(24 * startday)
		startday = startday + 30
	return hrs

def hourstomonths():
	""" Returns a list of month abbreviations. """
	month = [] 
	for x in range(1, 13):
		month.append(calendar.month_abbr[x])
	return month

