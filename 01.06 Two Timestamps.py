print("first timestamps")
hours1 = int(input("enter hours: "))
minutes1 =int(input("enter minutes: "))
seconds1 = int(input("enter seconds: "))
print("second timestamps")
hours2 = int(input("enter hours: "))
minutes2 = int(input("enter minutes: "))
seconds2 = int(input("enter seconds: "))

time1 = (hours1 * 60 * 60) + (minutes1 * 60) + seconds1
time2 = (hours2 * 60 * 60) + (minutes2 * 60) + seconds2
diff = time2 - time1
print(diff)
