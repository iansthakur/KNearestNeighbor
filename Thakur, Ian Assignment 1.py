import math
import csv





#newPoint is the list of data points of the data that needs to be categorized
#oldPoint is the list of data points of the already classified data
def calcDistance(newPoint, oldPoint):
	dist = 0
	i = 0 # might need to change this to 1 if I want new point to maintain the id term in its first spot 
	if len(newPoint) != len(oldPoint):
		# print("data is of wrong dim")
		return -1 #what should return be?-- currently i return 0 but that is misleading

	for coordinate in newPoint:
		# print dist
		# print coordinate
		if(i != (len(newPoint)-1)) and (i!=0): 
		#ignore first and last bc they are ID and classification not coordinates
			dist+= math.pow ((coordinate-oldPoint[i]),2)
			i+=1
		else:
			i+=1
	dist = math.sqrt(dist)
	# print dist
	return dist

#data is the .data file with all of the different data points
#returns a list of data points
def loadData(given):
	f = open(given, 'r')
	# print (f.readline())
	# print (f.readline())
	#print(f.read())
	list1 = []

	for row in f:
		a = ''
		list2 = []
		for c in row:
			if c != ',' and c!= '\n' :
				if (c=='?'):
					a+= "0"
				else:
					a+=c
				# a+=c
			else:
				x = int(a)
				list2.append(x)
				a=''
		list1.append(list2)

	# print (list1)
	f.close
	return list1

#unclassified is the .txt file of data that needs to be classified
#classified is the .data file of data that has already been classified
def classifyData(unclassified, classified,k):
	allPoints = loadData(classified)
	data = loadData(unclassified)
	# print allPoints
	# print data
	# # allPoints = classified
	# data = unclassified
	for point in data:
		findNN(point, allPoints,k)

	print("done")



#generates a list of points 
#where points are a list of coordinates
#this is just for my testing
def generateList(a, b, c, d):
	return (a,b,c,d)


#newPoint is the list of data points of the data that needs to be categorized
#oldPoint is the list of data points of the already classified data
#classifies the newPoint by its nearest neighbor
def findNN(newPoint, allPoints,k):
	redCount = 0
	greenCount = 0
	error = 0
	# counter = 0
	lastElementIndex = len(newPoint)-1
	dist = []
	# print("length is ", lastElementIndex)
	# print newPoint
	# holdMin = calcDistance(newPoint,allPoints[0])
	for current in allPoints:
		trial = calcDistance(newPoint, current)
		# print trial
		if trial<0:
			error+=1
			# print "hi :)"
			# error = True
			# break;
		else:
			# print counter
			dist.append((trial,current[lastElementIndex]))
			# counter+=1
	# print dist
	# print "doing something"
	dist.sort(key=lambda x:x[0])
	# print dist

	if not len(dist) < 3:
		for i in range (k):
			# print dist
			# print i
			if dist[i][1] == 2 :
				redCount+=1
			else :
				greenCount+=1

	#if you wanted me to write to the file, i would do that here
	#i have opted to just print it out 
	if redCount > greenCount:
		print (newPoint[0], " is benign")
	elif redCount == greenCount:
		print ("There was an error processing ", newPoint[0])
	else:
		print (newPoint[0], " is malignant")


# # print ("hello world")
# u1 = (111,7,4,3,0)
# u2 = (222,2,2,0)
# u3 = (333,4,6,7,0)
# u4 = (444,15,3,5,0)
# p1 = (666,17,6,2,2) #red
# p2 = (777,10,3,1,2) #red
# p3 = (888,4,6,7,4) #green
# p4 = (999,1,1,1,4) #green
# a = generateList(u1,u2,u3,u4)
# b = generateList(p1,p2,p3,p4)
print("Input original data file name as '<FileName>' : ")
originalData = input()
# print originalData
print("Input new data file name as '<FileName>' : ")
testingFile = input()
print("what value of k")
k = input()
# originalData = "breast-cancer-wisconsin.data"
# testingFile = "TestingFile.csv"
# originalData = 'original.data'
# testingFile = 'test2.csv'
# k=3
#calcDistance(a,b)
#findNN(a,b)
#classifyData(a,b)
#alreadyClassified = loadData("breast-cancer-wisconsin.data")
classifyData(testingFile, originalData,k)
