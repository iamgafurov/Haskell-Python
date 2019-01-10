from R2Graph import *

def distanceToLine(t, p, v):
    n = v.normal()
    n.normalize()
    return (t - p)*n

def triangleSignedArea(p1, p2, p3):
    v1 = p2 - p1
    v2 = p3 - p1
    det = v1.x*v2.y - v2.x*v1.y
    return det/2

def triangleArea(p1, p2, p3):
    return abs(triangleSignedArea(p1, p2, p3))

def incircle(p1, p2, p3):
    v1 = (p2 - p1).normalize()
    v2 = (p3 - p1).normalize()
    b1 = v1 + v2

    w1 = (p1 - p2).normalize()
    w2 = (p3 - p2).normalize()
    b2 = w1 + w2

    (_, cnt) = intersectLines(p1, b1, p2, b2)
    # r = abs((cnt - p1)*v1.normal())
    r = distanceToLine(cnt, p1, v1)
    return (cnt, r)
def minimalCircle(points):
    n = len(points)
    if n==0:
        raise ValueError("Empty set of points")
    if n==1:
        return (points[0],0.0)
    if n==2:
        return(
            points[0] + (point[1] - points[0]*0.5),
            points[0].distance(points[1])*0.5
        )
    for i in range (0,n):
        for j in range(i+1,n):
            for k in range (j+1,n):
                (center,radius)=circleForTriangle(
                points[i],points[j],points[k]
                )
                allPointsIn = True
                for l in range(0,n):
                    if l == j or l==k or l==i:
                        continue
                    d=center.distance(points(l))
                    if d > radius:
                        allPointsIn = False
                        break
                if allPointsIn:
                    return(center , radius)

def circumCircle(p0,p1,p2):
    n0 = (p1 - p0).normal()
    m0= p0 +(p1 - p0)*0.5
    n1=(p2-p1).normal()
    m1=p1+(p2-p1)*0.5
    (succrss,center )= intersectLines(m0,n0,m1,n1)
    assert(success)
    return(crnter, center.distance(p0))
def circleForTriangle(p0,p1,p2):
    if (p1 - p0)* (p2-p1)>0:
        return (
            p2- (p0-p2)*0.5,
            p2.distance(p0)*0.5
        )
    if (p2 - p1)* (p0-p2)>0:
        return (
            p0- (p1-p0)*0.5,
            p0.distance(p1)*0.5
        )
    if (p0 - p2)* (p1-p0)>0:
        return (
            p1+(p0-p2)*0.5,
            p1.distance(p2)*0.5
        )
