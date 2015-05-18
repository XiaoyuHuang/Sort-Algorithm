def bubble_sort(array):
	n = len(array)
	swap = True
	while swap:
		swap = False
		for i in range(1,n-1):
			if array[i-1] > array[i]:
				array[i-1],array[i] = array[i],array[i-1]
				swap = True
	return array

def main():
	array = [1,4,2,5,8,6,9]
	print  array
	newArray = bubble_sort(array)
	print newArray

if __name__ == "__main__":
	main()
