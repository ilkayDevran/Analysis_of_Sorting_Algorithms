import numpy as np
import matplotlib.pyplot as plt
import selection_sort
import insertion_sort
import MERGE
import time
def drawAllGraph():
	insertionTimes = []    #[0.0, 0.03, 9.9, 29.86] #10**k for k = 1,3,6,9
	selectionTimes = []
	mergeTimes = []		#[0.0, 0.0, 5.33, 29.9 ]
	arraySizes = [10**i for i in range(1,5)]
		
	for i in arraySizes:
		randomList = np.random.random_integers(1,10000000,size=i)	
		
		startTime = time.time()
		sel_list = selection_sort.selectionSort(np.random.random_integers(1,10000000,size=i))
		runTime = time.time()-startTime
		selectionTimes.append(runTime)
		
		startTime = time.time()
		merge_list = MERGE.mergeSort(np.random.random_integers(1,10000000,size=i))
		runTime = time.time()-startTime
		mergeTimes.append(runTime)
		
		startTime = time.time()
		insertion_list = insertion_sort.insertionSort(np.random.random_integers(1,10000000,size=i))
		runTime = time.time()-startTime
		insertionTimes.append(runTime)

	plt.figure(figsize=(12,5))
	plt.plot(arraySizes,selectionTimes,marker='x',c='b',label='Selectionsort')
	plt.plot(arraySizes,mergeTimes,marker='x',c='r',label='Mergesort')
	plt.plot(arraySizes,insertionTimes,marker='x',c='g',label='Insertionsort')
	plt.xscale('log')
	plt.yscale('log')
	plt.xlabel("size of unsorted list - log scale")
	plt.ylabel("seconds of computation - log scale")
	plt.legend(loc=2)
	plt.grid()
	plt.title("Selectionsort vs Mergesort vs Insertionsort")
	plt.show()

#http://nixonite.github.io/posts/complexity-of-algorithms-with-python.html