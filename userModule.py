import inputValues
print(inputValues.lowerlimit)

inputValues.lowerlimit = [10, 100, 1000, 10000, 100000, 100000]
inputValues.upperlimit = [20, 200, 2000, 20000, 200000, 200000]
# Test Input List
inputValues.value = [15, 105, 1005, 10005, 100005, 100005]
def checkRange(index, num):
# using comaparision operator
   if inputValues.lowerlimit[index] <= num <= inputValues.upperlimit[index]:
      print('The value {} is in range ({}, {})'.format(num, inputValues.lowerlimit[index], inputValues.upperlimit[index]))
   else:
      print('The value {} is not in range ({}, {})'.format(num, inputValues.lowerlimit[index], inputValues.upperlimit[index]))

#send values to comparison uperator
for i, val in enumerate(inputValues.value):
  print ('The input no is {} and the value is {}'.format(i , val))
  checkRange(i, val)
