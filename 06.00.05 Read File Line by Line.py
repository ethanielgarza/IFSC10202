# Open a file for reading
demotextfile = open("06.00.00 DemoText.txt")
# Read the first line of the file
x = demotextfile.readline()
# End of file is indicated when the input is empty
while x != "":
# Print the contents - Note the embedded linefeeds
	print(x)
# Read the next line of the file
	x = demotextfile.readline()
# Close the file
demotextfile.close()

# Open a file for reading
demotextfile = open("06.00.00 DemoText.txt")
# Read through the file
for x in demotextfile:
# Print the contents - Note the imbedded linefeeds
	print(x)
# Close the file
demotextfile.close()