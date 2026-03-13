year = 1950
if year > 1980 and year < 1990:
    print ("You were born in the 80's")
elif year > 1990 and year < 2000:
    print ("You were born in the 90's")
else:
    print ("You were not born in either the 80's or 90's")


expenses = 54
people = 2
if people >= 15:
    percentage = 0.15
elif people > 6:
    percentage = 0.10
else:
    percentage = 0
tip = expenses * percentage
bill = expenses + tip
print ("Total bill:", bill)


