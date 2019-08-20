
import numpy

m1 = numpy.matrix('1,2,3;4,5,6;7,8,9')
m2 = numpy.matrix('1,2,3;4,5,6;7,8,9')

m3 = m1 * m2                                #Matrix Multiplication Directly

print(m3)

#Matrix multiplication using loops

z1 = numpy.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
z2 = numpy.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

z3 = numpy.array([
    [0,0,0],
    [0,0,0],
    [0,0,0]
])

k=0
for i in range(3):
    for j in range(3):
        for k in range(3):
         z3[i][j] = z3[i][j] + (z1[i][k]*z2[k][j])

print(z3)