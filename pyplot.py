
import selection_sort
import insertion_sort
import MERGE
import allInOne
import time

size = 0
rng = 0
def Main():
	print """\nChoose type of sort to get runtime with spesific variables
	1. Insertion sort 
	2. Selection Sort
	3. Merge Sort
	4. Draw all of their run time graph with 10**k where k = 1,2,3,4,5
	"""
	x = int(raw_input('>>> '))
	if x == 4:
		chooseSortType(x, generateRandomArrays(1,1))
	else:
		size = setSize()
		rng = setRange()
		print '\n','Array Size: ', 10**size, "Range 0 -",10**rng
		createArray = generateRandomArrays(10**rng,10**size)
		chooseSortType(x, createArray)

def generateRandomArrays(length,rng):
	from random import randint
	List=[randint(0,length) for i in range(rng)]
	return List

def callInsertionSort(list):
	start_time = time.time()
	insertion_sort.insertionSort(list)
	insertionSort_time = (time.time() - start_time)
	print("\nInsertion Sort --- %s  ---\n" % insertionSort_time)
	#print(list)
	print("\n")

def callSelectionSort(list):
	start_time = time.time()
	selection_sort.selectionSort(list)
	selectionSort_time = (time.time() - start_time)
	print("\nSelection Sort --- %s  ---\n" % selectionSort_time)
	#print(list)
	print("\n")

def callMergeSort(list):
	start_time = time.time()
	MERGE.mergeSort(list)
	mergeSort_time = (time.time() - start_time)
	print("\nMerge Sort --- %s  ---\n" % mergeSort_time)
	#print(list)
	print("\n")

def setSize():
	try:
		return int(raw_input('Enter the array size (10**size): '))
	except ValueError:
		print "Not a number"
		return 0

def setRange():
	try:
		return int(raw_input('Define the range (0 to ...): '))
	except ValueError:
		print "Not a number"
		return 0

def chooseSortType(x,list):
	if x == 1: 
		return callInsertionSort(list)
	elif x == 2:
		return callSelectionSort(list)
	elif x == 3:
		return callMergeSort(list)
	elif x == 4:
		return allOFthem()
	else:
		print "Wrong sort code"
		return


def allOFthem():
	allInOne.drawAllGraph()


if __name__ == '__main__':
	Main()






