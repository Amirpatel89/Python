fullName = "Amir Patel"	
age = 28
myArray = [];
myArray.append(fullName)
myArray.append(age)
print myArray
def sayHello():
	print "Hello!"
sayHello()
splitName = fullName.split()
print splitName
def sayName():
	print "Hello, %s" % splitName[0]
sayName()
import datetime
now = datetime.datetime.now()
currentYear = now.year
def myAge(yearBorn):
	print (currentYear - yearBorn)
myAge(1989)

def sum_odd_numbers():
	sum = 0
	for i in range(1, 5001):
		if (i % 2 == 1):
			sum += i
	print sum
sum_odd_numbers()

def sum_odd_numbers2():
	sum = 0
	for i in range(1, 5001, 2):
		if (i % 2 == 1):
			sum +- i
	print sum
sum_odd_numbers2()

def sum_odd_numbers3():
	i = 1
	sum = 0
	while 1:
		sum += i
		if (i == 5000):
			break