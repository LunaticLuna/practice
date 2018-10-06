#recursive fibonacci:
def recFib(n):
	if n <= 2 :return 1
	return recFib(n-1) + recFib(n-2)

#dp fibonacci:
def bottomUpFib(n):
	if n <= 2: return 1
	a,b = 1,1

	for i in xrange(3,n+1):
		a,b = b,a+b
	return b


n = 14
#1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377
print recFib(n),bottomUpFib(n)
