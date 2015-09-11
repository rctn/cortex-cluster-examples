import numpy as np
import theano
import timeit

d = 1000
X = np.random.randn(d,d)
Y = np.random.randn(d,d)

print 'Testing numpy'
start = timeit.default_timer()
Z = np.dot(X, Y)
end = timeit.default_timer()
print "Took {0:.0f} seconds".format(end-start)

print 'Testing theano'
t_X = theano.tensor.matrix('X')
t_Y = theano.tensor.matrix('Y')
t_Z = theano.tensor.dot(t_X, t_Y)
mult = theano.function(inputs=[t_X, t_Y],
		       outputs=[t_Z])

start = timeit.default_timer()
Z = mult(X, Y)
end = timeit.default_timer()
print "Took {0:.0f} seconds".format(end-start)
