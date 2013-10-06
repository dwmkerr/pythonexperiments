# Pascals Triangle
#
# The code experiment is a learning exercise for Python.

# Declare the number of rows we'll draw
rowCount = 10

# Create storage for the rows
rows = [[1]]

# Create each row.
currentRow = 1
while(currentRow <= rowCount):
	
	# Create a row.
	row = []

	# Number of elements rowcount and another (to make the triangle shape).
	elementCount = currentRow + 1
	
	# Add each element.
	currentElement = 0
	while currentElement < elementCount:

		val = 0

		# Element is sum of parent and next.]
		if currentElement is 0:
			val=rows[currentRow-1][0]
		elif currentElement >= len(rows[currentRow-1]):
			val=rows[currentRow-1][-1]
		else:
			val=rows[currentRow-1][currentElement] + rows[currentRow-1][currentElement-1]

		row.append(val)

		# Next element
		currentElement = currentElement+1

	# Add the row.
	rows.append(row)

	# Next row.
	currentRow = currentRow+1

# Print each row.
for row in rows:
	print(row)