#Write function that converts a temperature from degrees Kelvin to degrees Fahrenheit
try:
	k=int(input("Enter temp in Kelvin: "))
	f=(k - 273.15) * 9/5 + 32
	print("Temp in Fahrenheit: ",f)
except:
	print("Error")
	