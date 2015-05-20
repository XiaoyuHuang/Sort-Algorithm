def quick_sort(array):
	n = len(array)
	return qsort(array, 0, n-1)

def qsort(array, l, r):
	if l > r:
		return
	key = array[l]
	lp = l
	rp = r
	while lp < rp:
		while array[rp] >= key and lp < rp:
			rp = rp - 1
		while array[lp] <= key and lp < rp:
			lp = lp + 1
		array[lp], array[rp] = array[rp], array[lp]
	array[l], array[lp] = array[lp], array[l]
	qsort(array, l, lp-1)
	qsort(array, rp+1, r)
	return array


def main():
	array = [1,7,4,2,5,8,6,9]
	print  array
	newArray = quick_sort(array)
	print newArray

if __name__ == "__main__":
	main()
