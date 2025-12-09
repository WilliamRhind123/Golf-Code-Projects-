MyList = []
y = 2
x = 2
while y < 50:
	if y < x or y == x:
		LeylandNum = (x**y) + (y**x)
		#print(LeylandNum, x, y)
		if LeylandNum not in MyList and LeylandNum < 100000000000:
			MyList.append(LeylandNum)
		if x < 50:
			x+=1
		if x == 50:
			y+=1
			x=(y)

MyList.sort()
for i in MyList:
	print(i)