def merge_sort(array):
	n = len(array)
	if n <= 1:
		return array
	mid  = n/2
	left = array[0:mid]
	right = array[mid:]
	left = merge_sort(left)
	right = merge_sort(right)
	newArray = merge(left, right)
	return newArray

def merge(left, right):
	array = []
	ileft = 0
	iright = 0
	while ileft < len(left) and iright < len(right):
		if left[ileft] < right[iright]:
			array.append(left[ileft])
			ileft = ileft+1
		else:
			array.append(right[iright])
			iright = iright+1
	while ileft < len(left):
		array.append(left[ileft])
		ileft = ileft + 1
	while iright < len(right):
		array.append(right[iright])
		iright = iright + 1

	return array

def main():
	array = [1,7,4,2,5,8,6,9]
	print  array
	newArray = merge_sort(array)
	print newArray

if __name__ == "__main__":
	main()
