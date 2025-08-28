totalseconds = int(input("Enter a length of time in seconds: "))
secondsperminute = 60
minutesperhour = 60
hoursperday = 24
daysperyear = 365
#calculations
secondsperhour = secondsperminute * minutesperhour
secondsperday = secondsperhour * hoursperday
secondsperyear = secondsperday * daysperyear

years = totalseconds // secondsperyear
remiangsecondsafteryears = totalseconds % secondsperyear

days = remiangsecondsafteryears // secondsperday
remiangsecondsafterdays = remiangsecondsafteryears % secondsperday

hours = remiangsecondsafterdays // secondsperhour
remiangsecondsafterhours = remiangsecondsafterdays % secondsperhour

minutes = remiangsecondsafterhours // secondsperminute
seconds = remiangsecondsafterhours % secondsperminute

print(f"Years: {years}")
print(f"Days: {days}")
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")