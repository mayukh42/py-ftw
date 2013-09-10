import random
import math
import sys
import os
import re

# http://www.ualberta.ca/~hquamen/303/problems.html

# chr(x) return char of ascii code x
# ord(c) return ascii code of char c


# Caesar Cipher Encryption and Decryption
def caesar_enc(pt, k):
	ct = ''
	for c in pt:
		ct += str(chr((ord(c)+k - ord('a'))%26 + ord('a')))
	return ct

# print caesar_enc('abx', 13) # 'nok'

def caesar_dec(ct, k):
	pt = ''
	for c in ct:
		pt += str(chr((ord(c)-k - ord('a'))%26 + ord('a')))
	return pt

# print caesar_dec('nok', 13) # 'abx'


# Fibonacci Series (Using Matrix Multiplication)
def fib_mat(n):
	def mat_mult_2x2(A, B):
		C = [[0,0],[0,0]]
		for i in range(2):
			for j in range(2):
				for k in range(2):
					C[i][j] += A[i][k]*B[k][j]
		return C

	F = [[1,1],[1,0]]
	FN = F
	while n > 1:
		FN = mat_mult_2x2(FN, F)
		n -= 1
	return FN[1][1]

# print fib_mat(10) # 0,1,1,2,3,5,8,13,21,__34__,55,89,...
# print fib_mat(1000)

# Fibonacci Series (Using a List)
def fib_list(n):
	f = [0,1]
	while n > 1:
		f.append(f[-1]+f[-2])
		n -= 1
	return f[-2]

# print fib_list(10)
# print fib_list(1000)


# Random Frequency Distribution - Method 1
def rfd1(n, k):
	f = {i:0 for i in xrange(1, k+1)}
	for i in xrange(n):
		f[random.randint(1, k)] += 1
	return f

# print rfd1(100, 10)

# Random Frequency Distribution - Method 2
def rfd2(n, k):
	f = {i:0 for i in xrange(1, k+1)}
	for i in xrange(n):
		f[(random.randint(1, n)%10) + 1] += 1
	return f

# print rfd2(100, 10)


# Estimation of Pi using random numbers
# Imagine a dart game being played where the darts hit any point inside a square inscribed by a circle of radius r. Each side of square is thus 2r. The ratio of circle area to square area is pi/4. If we hit enough darts, we can find the ratio of darts inside the circle (area of circle) to total darts thrown (area of square). This multiplied by 4.0 gives an estimation of Pi.
def est_pi_rand(n):
	in_circle = 0
	total = n
	r = 64.0
	while n > 0:
		x = float(random.randint(0, int(r)))
		y = float(random.randint(0, int(r)))
		d = x**2 + y**2 # nullifies the need to have x,y in other 3 quadrants
		if d <= r**2:
			in_circle += 1
		n -= 1
	return 4.0*(float(in_circle)/total)

# print est_pi_rand(5000) # sample run: 3.1272
# print est_pi_rand(50) # sample run: 3.68
# print est_pi_rand(500000) # sample run: 3.10544


# Monte Carlo Gas Station
# Assumptions: 1 gas pump, entry-exit duration per customer: 8 mins, Pr[customer visiting gas stn] = 0.1
# Wait time of a customer excludes the 8 mins of service for that customer
def mcgs_avg_wait_time(hrs_open):	
	mins_open = hrs_open*60
	# print 'ideal # customers @ 8 min gap', mins_open/8
	customers = 0
	wait_time = 0
	total_wait_times = wait_time
	while mins_open > 0:
		visit_event = random.randint(1, 10)
		if visit_event == 1: # Pr = 0.1
			# customer visits gas stn
			customers += 1
			total_wait_times += wait_time # avg wait time excludes service time
			wait_time += 8			
			# total_wait_times += wait_time # avg wait time includes service time
		# clock ticks
		if wait_time > 0:
			wait_time -= 1
		mins_open -= 1
	print 'customers visited:', customers
	print 'overtime:', wait_time, 'mins' # remaining wait time
	print 'avg wait time:', total_wait_times/customers, 'mins' 

# mcgs_avg_wait_time(12) # gas stn open 12 hrs


# Primality Tests
# Prepared Sieve of Eratosthenes, longer the better (obviously)
def is_prime_naive(n):
	primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47.53,59,61,67,71,73,79,83,89,97]
	if n == 1:
		return False
	for p in primes:
		if n != p and n%p == 0:
			return False
	return True

# n = random.randint(1, 10000)
# print n, is_prime_naive(n) # pretty good
# print is_prime_naive(101*101) # fails here

# Fermat's Little Theorem: 
# a**n mod n == a mod n
# Technically, Fermat's test is a test for compositeness, rather than for primeness. This is because, if the test fails, the number is certainly composite, but if the test passes, the number is prime whp (might as well be a composite pseudoprime).
def is_prime_fermat(n):
	a = 2 # random.randint(2, n-1) # mathematically correct
	if (a**(n-1))%n == 1: # the beauty of arbitrary precision! Hail Monty!
		return True
	else:
		return False

# print n, is_prime_fermat(n)
# print is_prime_fermat(101*101)


# Text Processing

# Word Count: Frequency Distribution
# Stripping common words returns much better features of the text
common_words = {'a', 'an', 'the', 'it', 'in', 'to', 'of', 'when', 'what', 'how', 'than', 'who', 'i', 'he', 'she', 'they', 'them', 'then', 'if', 'you', 'and', 'that', 'for', 'is', 'are', 'was', 'were', 'your', 'can', 'could', 'should', 'would', 'shall', 'will', 'or', 'not', 'have', 'has', 'be', 'this', 'as', 'my', 'out', 'from', 'while', 'else', 'on', 'off', 'each', 'every', 'all', 'his', 'her', 'him', 'with', 'their', 'at', 'by', 'had', 'up', 'me', 'but', 'one', 'so', 'there', 'mr', 'well', 'yes', 'no', 'why', 'we', 'oh', 'do', 'here', 'ah', 'now', 'dr', 'miss', 'mrs', 'o'}

def word_count_map(txt_file):
	f = {}
	for line in txt_file:
		words = re.findall(r"[\w']+", line)
		# words = line.split() # naive split
		for word in words:
			if word in f:
				f[word] += 1
			elif word.lower() not in common_words and word[0].isupper():
				f[word] = 1
	return f

# os.chdir(dir) # to specify which directory to look in for the file
txt_file = open('G:\dev\data\sherlockholmes_acd.txt', 'r')
f = word_count_map(txt_file)
top_ten_words = sorted(f.iteritems(), key=lambda x: x[1], reverse=True)[:10]
print top_ten_words 
# Tom, Huck, Joe, Injun are top characters in Tom Sawyer
# Holmes, Sherlock, Watson, Street, Baker, London, Simon, Lestrade in SH
# Bloom, Stephen, John, Dedalus, Mulligan, Joe in Ulysses
# Alice, Queen, King, Turtle, Mock, Gryphon, Hetter, Rabbit in Wonderland