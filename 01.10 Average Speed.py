kilometers = int(input("enter length of race in kilometers: "))
minutes1 =int(input("enter minutes: "))
seconds1 = int(input("enter seconds: "))

miles = kilometers / 1.61
hr = (minutes1 / 60) + (seconds1 / 3600)
print (miles)