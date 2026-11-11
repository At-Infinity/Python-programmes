startyear=int(input("Enter the current year: "))
endyear=int(input("Enter a future year: "))
print("The future leap years are: ")
for year in range(startyear,endyear):
 if (year%4==0 and year%100!=0) or (year%400==0):
  print(year)

