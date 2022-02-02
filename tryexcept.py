def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None
		
x = "17"
y = "seveteen"

xInt = convert_number("17")
yInt = convert_number("seventeen")

print(x, xInt)
print(y, yInt)