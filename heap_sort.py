def heap_sort(array):
	n = len(array)
	heapify(array, n)
	end = n-1
	while end >= 0:
		swap(array, 0, end)
		end = end -1
		shiftDown(array, 0, end)
	return array

def heapify(array, count):
	start = (count-2)/2
	while start>=0:
		shiftDown(array, start, count-1)
		start = start - 1


def shiftDown(array, start, end):
	root = start
	while root*2+1 <= end:
		child = root*2+1
		needToSwap = root
		if array[needToSwap] < array[child]:
			needToSwap = child
		if child+1 <= end and array[needToSwap] < array[child+1]:
			needToSwap = child+1
		if needToSwap == root:
			return
		else:
			swap(array, root, needToSwap)
			root = needToSwap


def swap(array, idx1, idx2):
	tmp = array[idx1]
	array[idx1] = array[idx2]
	array[idx2] = tmp


def main():
	array = [1,4,2,5,8,6,9]
	print  array
	newArray = heap_sort(array)
	print newArray

if __name__ == "__main__":
	main()
