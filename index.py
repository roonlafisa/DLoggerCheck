# Given range
X = [10, 100, 1000, 10000, 100000, 100000]
Y = [20, 200, 2000, 20000, 200000, 200000]
# Test Input List
testInput = [15, 105, 1005, 10005, 100005, 100005]
def checkRange(index, num):
   # using comaparision operator
   if X[index] <= num <= Y[index]:
      print('The value {} is in range ({}, {})'.format(num, X[index], Y[index]))
   else:
      print('The value {} is not in range ({}, {})'.format(num, X[index], Y[index]))
      
      
for i, val in enumerate(testInput):
  print ('The input no is {} and the value is {}'.format(i , val))
  checkRange(i, val)
