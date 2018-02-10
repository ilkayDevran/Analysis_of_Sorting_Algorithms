def selectionSort(alist):
	for j in range(0,len(alist)-1):
		smallest = j
		for i in range(j+1,len(alist)):
			if alist[i] < alist[smallest]:
				smallest = i
		temp = alist[j]
		alist[j] = alist[smallest]
		alist[smallest] = temp