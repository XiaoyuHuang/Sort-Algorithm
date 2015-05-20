def shell_sort(array):
	n = len(array)
	gap = round(n/2)
	while gap > 0:
		for i in range(gap, n):
			tmp = array[i]
			j = i
			while j>= gap and array[j-gap] > tmp:
				array[j] = array[j - gap]
				j = j- gap
			array[j] = tmp
		gap = round(gap/2)
	return array

def main():
	array = [1,4,2,5,8,6,9]
	print  array
	newArray = shell_sort(array)
	print newArray

if __name__ == "__main__":
	main()
