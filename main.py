# -*- coding:UTF-8-*-
# coding: UTF-8
import random

__author__ = 'nakaji'

print "Hello, world!"
print u'こん¥u0020にちは'

print '-----'
a = ['dog', 'cat', 'panda']
for x in a:
    print x, len(x)
print '-----'
#abc = ['1', '2', '3']
#abc = [1, 2, 3]
abc = [0]

abc[0] = 1
for x in abc:
    print x#, len(x)
print '-----'

#exit()

# Fibonacci 級数
print u'Fibonacci級数、始まり'
a, b, c = 0, 1, 1
while b < 10:
    print str(b) + ' ' + str(c)
    a, b = b, a + b
    c += 1
print u'Fibonacci級数は、おしまい'



# if
print 'If　始まり'
c = 0
counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#counts[2] = 2
#print counts[10]
#print counts[2]
#exit()

while c < 10000:
    r = int(random.random() * 10 + 1)
    #print r
    print '%2d, ' %r
    counts[r] = counts[r] + 1
    for i in range(len(counts)):
        print '%d, ' %(counts[i]),
#        print i
    print ''
    c += 1


print
s = 0
for i in range(len(counts)):
    s = s + counts[i]
print 'sum=' + str(s)
for i in range(len(counts)):
    print '%d%%, ' %(counts[i] * 100 / s ),

