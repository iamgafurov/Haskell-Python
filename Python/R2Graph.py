'''
Classes supporting a geometry on R2 plane:
    R2Vector, R2Point
'''
from math import sqrt, atan2

class R2Vector(object):
    """Vector on R2-Plane"""

    def __init__(self, x = 0., y = 0.):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, v):
        assert type(v) == R2Vector
        return R2Vector(self.x + v.x, self.y + v.y)

    def __iadd__(self, v):
        assert type(v) == R2Vector
        self.x += v.x; self.y += v.y
        return self

    def __sub__(self, v):
        assert type(v) == R2Vector
        return R2Vector(self.x - v.x, self.y - v.y)

    def __isub__(self, v):
        assert type(v) == R2Vector
        self.x -= v.x; self.y -= v.y
        return self

    def __mul__(self, v):
        if type(v) == R2Vector:
            """Scalar product of 2 vectors"""
            return self.x * v.x + self.y * v.y
        else:
            """Multiply a vector by a number"""
            return R2Vector(self.x*float(v), self.y*float(v))

    def __imul__(self, a):
        """Multiply a vector by a number"""
        # return R2Vector(self.x*float(a), self.y*float(a))
        self.x *= float(a)
        self.y *= float(a)
        return self

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):
        return "(" + repr(self.x) + ", " + repr(self.y) + ")"

    def length(self):
        return sqrt(self.x*self.x + self.y*self.y)

    def normalize(self):
        ''' Normalization of vector: make its length == 1
        preserving its direction'''
        l = self.length()
        if l > 0.:
            self.x /= l
            self.y /= l
        return self

    def normal(self):
        return R2Vector(-self.y, self.x)

    def angle(self, v):
        '''Angle between two vecctors in radians'''
        xx = v*self
        yy = v*self.normal()
        return atan2(yy, xx)

class R2Point(object):
    """Point on R2-Plane"""

    def __init__(self, x = 0., y = 0.):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, v):
        assert type(v) == R2Vector
        return R2Point(self.x + v.x, self.y + v.y)

    def __iadd__(self, v):
        assert type(v) == R2Vector
        self.x += v.x; self.y += v.y
        return self

    def __sub__(self, v):
        if type(v) == R2Vector:
            return R2Point(self.x - v.x, self.y - v.y)
        else:
            assert type(v) == R2Point
            return R2Vector(self.x - v.x, self.y - v.y)

    def __isub__(self, v):
        assert type(v) == R2Vector
        self.x -= v.x; self.y -= v.y
        return self

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):
        return "(" + repr(self.x) + ", " + repr(self.y) + ")"

def intersectLines(p1, v1, p2, v2, eps=1e-8):
    """Intersect straight lines

    Each line is defined by a pair (point, vector).
    Return value is a tuple (True/False, P):
    True if the lines intersect, False if they are
    parallel; if lines intersect, then P is a point
    of their intersection"""
    n = v1.normal()
    s = n*v2
    if abs(s) <= eps:
        return False, R2Point()
    t = n*(p1 - p2) / s
    p = p2 + v2*t
    return True, p
