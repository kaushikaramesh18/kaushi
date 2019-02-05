year =int(input("please enter the year number you wish:"))
if(year%400 ==0):
print("%d is a leap year"%year)
elif(year%100 ==0):
print("%d is not the leap year" %year)
elif(year %4== 0):
print("%d is a leap year"%year)
else:
print("%d is not the leap year" %year)
