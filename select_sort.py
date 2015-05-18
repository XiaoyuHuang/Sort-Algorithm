def select_sort(array):
	n = len(array)
	imin = 0
	for i in range(n-1):
		imin = i
		for j in range(i+1, n):
			if array[j] < array[imin]:
				imin = j
		if imin != i:
			tmp = array[i]
			array[i] = array[imin]
			array[imin] = tmp
	return array

def main():
	array = [1,4,2,5,8,6,9]
	print  array
	newArray = select_sort(array)
	print newArray

if __name__ == "__main__":
	main()
