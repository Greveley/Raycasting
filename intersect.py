# def intersect(x1,y1,x2,y2,x3,y3,x4,y4):
#
#     den = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
#
#     if den == 0:
#         return False
#
#     num1 = (x1-x3)*(y3-y4)-(y1-y3)*(x3-x4)
#     t = num1/den
#
#     num2 = (x1-x2)*(y1-y3)-(y1-y2)*(x1-x3)
#     u = -1*(num2/den)
#
#     print x2,y2
#
#     if t>0 and t<1 and u>0:
#         return True
#     else:
#         return False

def intersect(Ax1, Ay1, Ax2, Ay2, Bx1, By1, Bx2, By2):
    """ returns a (x, y) tuple or None if there is no intersection """
    d = (By2 - By1) * (Ax2 - Ax1) - (Bx2 - Bx1) * (Ay2 - Ay1)
    if d:
        uA = ((Bx2 - Bx1) * (Ay1 - By1) - (By2 - By1) * (Ax1 - Bx1)) / d
        uB = ((Ax2 - Ax1) * (Ay1 - By1) - (Ay2 - Ay1) * (Ax1 - Bx1)) / d
    else:
        return False
    if not (0 <= uA <= 1 and 0 <= uB <= 1):
        return False
    x = Ax1 + uA * (Ax2 - Ax1)
    y = Ay1 + uA * (Ay2 - Ay1)
    #
    return x, y

def intersect_points(Ax1, Ay1, Ax2, Ay2, Bx1, By1, Bx2, By2):
    """ returns a (x, y) tuple or None if there is no intersection """
    d = (By2 - By1) * (Ax2 - Ax1) - (Bx2 - Bx1) * (Ay2 - Ay1)
    if d:
        uA = ((Bx2 - Bx1) * (Ay1 - By1) - (By2 - By1) * (Ax1 - Bx1)) / d
        uB = ((Ax2 - Ax1) * (Ay1 - By1) - (Ay2 - Ay1) * (Ax1 - Bx1)) / d
    if (0 <= uA <= 1 and 0 <= uB <= 1):
        x = Ax1 + uA * (Ax2 - Ax1)
        y = Ay1 + uA * (Ay2 - Ay1)
        return x, y














