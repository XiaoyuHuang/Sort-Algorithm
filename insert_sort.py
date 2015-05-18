def insert_sort(array):
	n = len(array)
	swap = True
	for i in range(1, n):
		if array[i-1] > array[i]:
			tmp = array[i]
			for j in range(i-1, -1, -1):
				if array[j] > tmp:
					array[j+1] = array[j]
					idx = j
				else:
					break
			array[idx] = tmp
	return array

def main():
	array = [1,4,2,5,8,6,9]
	print  array
	newArray = insert_sort(array)
	print newArray

if __name__ == "__main__":
	main()
