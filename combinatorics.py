# combinatorics.py 

def subsets(xs):
    acc = []
    def s_rec(soFar, rest):
        if rest == '':
            acc.append(soFar)
        else:
            s_rec(soFar + rest[0], rest[1:])
            s_rec(soFar, rest[1:])
    s_rec('', xs)
    return acc

def permutations(xs):
    acc = []
    def p_rec(soFar, rest):
        if rest == '':
            acc.append(soFar)
        else:
            for i in range(len(rest)):
                p_rec(soFar+rest[i], rest[:i]+rest[i+1:])
    p_rec('', xs)
    return acc

def factorial(n):
    def fact_rec(m, acc):
        if m <= 1:
            return acc
        else:
            return fact_rec(m-1, acc*m)
    return fact_rec(n, 1)

s = 'abcde'
# print len(subsets(s))==(1<<len(s))
# print len(permutations(s))==factorial(len(s))
