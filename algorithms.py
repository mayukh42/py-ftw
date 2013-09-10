import sys
import random

def binary_search(a, l, u, key):
	if l > u:
		return 'Not found'
	else:
		mid = (l+u)/2
		if a[mid] == key:
			return 'Found at position', mid
		elif a[mid] < key:
			return binary_search(a, mid+1, u, key)
		else:
			return binary_search(a, l, mid-1, key)

a = list(range(100))
# print binary_search(a, 0, len(a)-1, 100)

def reverse_list_fp(a):
	def rlf_rec(arr, acc):
		if len(arr) < 1:
			return acc
		else:
			acc = [arr[0]]+acc
			return rlf_rec(arr[1:], acc)
	return rlf_rec(a, list())
# 
# print reverse_list_fp(a)

def permutations(s):
	def rec_permute(soFar, rest):
		if rest == '':
			print soFar
		else:
			for i in range(len(rest)):
				rec_permute(soFar + rest[i], rest[:i]+rest[i+1:])
	rec_permute('', s)

s = 'abcd'
# print permutations(s)

def subsets(s):
	def rec_subsets(soFar, rest):
		if rest == '':
			print soFar
		else:
			rec_subsets(soFar+rest[0], rest[1:])
			rec_subsets(soFar, rest[1:])
	rec_subsets('', s)

# print subsets(s)

def maximal_sum(a):
	maxsum = 0
	maxsofar = 0 # max sum for empty list
	for i in range(len(a)):
		maxsofar = max(maxsofar+a[i], 0)
		maxsum = max(maxsum, maxsofar)
	return maxsum

bs = [-1,-2,-3,-4,-5]
bentley = [31,-41,59,26,-53,58,97,-93,-23,84]
# print maximal_sum(a)
# print maximal_sum(bs)
# print maximal_sum(bentley)

def qsort(a):
	def qsort_rec(xs):
		if xs == []:
			return xs
		p = random.randint(0, len(xs)-1)
		xs[0], xs[p] = xs[p], xs[0]
		le = [x for x in xs[1:] if x <= xs[0]]
		gt = [x for x in xs[1:] if x > xs[0]]
		return qsort_rec(le) + [xs[0]] + qsort_rec(gt)
	return qsort_rec(a)

bad_list = [random.randint(0,x) for x in range(1000)]
# print qsort(bad_list)
# n = 10e5: 12.9s
# n = 10e4: 1.2s
# n = 10e3: 0.3s

# ss0 = sorted([i for i in range(100000)]) # 0.3 s
# ss1 = sorted([i for i in range(1000000)]) # 0.6 s
# ss2 = sorted([i for i in range(10000000)]) # 3.6 s

def suffix_array(ss):
	# This is just a conceptual implementation; the real suffix arrays are not supposed to contain copies of the substrings as this one, so the below will take forever for illiad.
	sa = [ss[i:] for i in xrange(len(ss))]
	sa.sort()
	return sa

# sfs = suffix_array('banana')
# print sfs

def lcp(xs, ys):
	if len(xs) < len(ys):
		if ys[:len(xs)] == xs:
			return xs
	else:
		if xs[:len(ys)] == ys:
			return ys
	return ''

# print lcp('banana', 'anana')

def longest_repeated_string(ss):
	sfs = suffix_array(ss)
	lr_in_pairs = [lcp(sfs[i], sfs[i+1]) for i in xrange(len(ss)-1)]
	return max(lr_in_pairs, key=lambda x: len(x))

# print longest_repeated_string('banana')

# inp = open('iliad.mb.txt', 'r')
# the_iliad = inp.read()
# print longest_repeated_string(the_iliad)

def qsort3(a, l, u):
	if l > u:
		return
	p = a[l]
	i = l+1
	j = u
	while True:
		while i < u and a[i] <= p:
			i += 1
		while j > l and a[j] > p:
			j -= 1
		if i > j:
			break
		a[i], a[j] = a[j], a[i]
	a[j], a[l] = a[l], a[j]
	qsort3(a, l, j-1)
	qsort3(a, j+1, u)

# print qsort3(bentley, 0, len(bentley)-1)

# xs = [2] # len = 7
# i = 6 # i = 0
# print xs[:i]+xs[i+1:]
# max_err = 1.0e-14
# print max_err

# mydict = {1:0, 2:3, 3:4, 5:6}
# print mydict.pop(1, None)
# print mydict

def simple_sprintf(*args):
	# 'first name is %s, last name is %s', 'alice', 'bob'
	s = args[0]
	vs = args[1:]
	ret = ''
	keys = {'s', 'd', 'f'}
	i = 0
	j = 0
	while i < len(s):
		if s[i] == '%' and i < len(s)-1 and j < len(vs) and s[i+1] in keys:
			ret += str(vs[j])
			j += 1
			i += 1
		else:
			ret += s[i]
		i += 1
	if j != len(vs):
		return 'incorrect sprintf expression'
	return ret

# print simple_sprintf('first name is %s, last name is %s', 'alice', 'bob')

def multi_args(*args):
	# args: array
	print 'called with', len(args), 'args'
	print 'args:', args

# multi_args(1, 2)
# multi_args('hello', 'world', 2, 5)

def multi_kv_args(**kvs):
	# kvs: dict
	for k, v in kvs.iteritems():
		print k, ':', v

# multi_kv_args(abc=123, efg=567, gh='gh')

def mix_args(*args, **kvs):
	for a in args:
		print a
	for k, v in kvs.iteritems():
		print k, ':', v

# mix_args(1, 2, 3, apple=111, coconut='coconut', banana=222)
# args must be followed by k,v pairs, no mix and match there

def fib_iter(n):	
	a, b = 0, 1
	j = 1
	while j < n:
		a, b = b, a+b
		j += 1
	return a

# print fib_iter(10)

def mat_mult(A, B):
	# trivial O(n**3)
	if len(A[0]) != len(B):
		print 'error: dimensions mismatch'
		return None
	C = [[0 for j in xrange(len(B[0]))] for i in xrange(len(A))]
	for i in xrange(len(A)): # rows in A
		for j in xrange(len(B[0])):
			for k in xrange(len(A[0])):
				C[i][j] += A[i][k] * B[k][j]
	return C

def mat_toStr(A):
	for i in xrange(len(A)):
		for j in xrange(len(A[0])):
			print A[i][j],
		print ''

# A = [[1, 1], [1, 0]]
# I = [[1, 0], [0, 1]]
# mat_toStr(mat_mult(A, I))

def fib_mat(n):
	F = [[1, 1], [1, 0]]
	A = F
	j = 1
	while j < n:
		A = mat_mult(A, F)
		j += 1
	return A[1][1]

def fib_tests(n):
	for i in xrange(n):
		if fib_iter(i) != fib_mat(i):
			return 'failed at ' + str(i)
	return 'passed for all n'

# print fib_tests(100)