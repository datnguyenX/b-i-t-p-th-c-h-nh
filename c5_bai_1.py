def square(n):
    returnn*n
def cube(n):
    return n*n*n
def average(values):
    nvals = len(values)
    sum = 0.0
    for v in values:
        sum += v
    return float(sum)/nvals

import mymath 
values = [2,4,6,8,10]
print('square:')
for v in values:
    print(mymath.square(v))
    print('Cubes:')
for v in values:
    print(mymath.cube(v))
print('Average:' + str(th.average(values)))
