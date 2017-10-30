from math import hypot
class Vector(object):
	
	'''
	>>> v1 = Vector(3, 4)
	>>> abs(v1 * 3)
	15.0
	'''
	
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		
	def __repr__(self):
		return 'Vector(%r, %r)' % (self.x, self.y)
		
	def __abs__(self):
		return hypot(self.x, self.y)
		
	def __bool__(self):
		return bool(abs(self))
		
	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x, y)
		
	def __mul__(self, scalar):
		return Vector(self.x * scalar, self.y * scalar)
		
		
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)