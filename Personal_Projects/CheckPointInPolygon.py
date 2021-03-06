def onSegment(x, y, z):
    if y[0] <= max(x[0], z[0]) and y[0] >= min(x[0], z[0]) and y[1] <= max(x[1], z[1]) and y[1] >= min(x[1], z[1]):
        return True

    return False

# To find orientation of ordered triplet (p, q, r).
# The function returns following values
# 0 --> all points are collinear
# 1 --> x, y and z oriented clockwise
# 2 --> x, y and z oriented counterclockwise
def orientation(x, y, z):
    val = ((y[1] - x[1]) * (z[0] - y[0])) - ((y[0] - x[0]) * (z[1] - y[1]))

    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

# The main function that returns true if line segment 'p1q1'  and 'p2q2' intersect.
def checkIntersection(x1, y1, x2, y2):

    # Find four orientations needed for general and special cases
    o1 = orientation(x1, y1, x2)
    o2 = orientation(x1, y1, y2)
    o3 = orientation(x2, y2, x1)
    o4 = orientation(x2, y2, y1)

    # General case
    if (o1 != o2 and o3 != o4):
        return True

    # Special cases

    # x1, y1 and x2 are collinear and x2 lies on segment x1-y1
    if (o1 == 0 and onSegment(x1, x2, y1)):
        return True

    # x1, y1 and x2 are collinear and q2 lies on segment x1-y1
    if (o2 == 0 and onSegment(x1, y2, y1)):
        return True

    # x2, y2 and x1 are collinear and x1 lies on segment x2-y2
    if (o3 == 0 and onSegment(x2, x1, y2)):
        return True

    # x2, y2 and y1 are collinear and y1 lies on segment x2-y2
    if (o4 == 0 and onSegment(x2, y1, y2)):
        return True

    # Doesn't fall in any of the above cases
    return False

def isInside(polygon, n, p):

    # Polygon must have >= 3 vertices
    if n < 3:
        return False

    # extend the given point to the right all the way to infinity
    extended_line = [10000, p[1]]

    # Count intersections of extended line with sides of polygon
    count = 0
    i = -1

    while i != 0:

        if i < 0:
            i = 0

        next = (i+1) % n

        # Check if extended line from p intersects with line segment from polygon[i] to polygon[next]
        if checkIntersection(polygon[i], polygon[next], p, extended_line):

            # If p is collinear with line segment i-next, check if p lies on the segment
            # If p lies on the segment, return true. Otherwise, return false
            if orientation(polygon[i], p, polygon[next]) == 0:
                return onSegment(polygon[i], p, polygon[next])

            count = count + 1

        i = next


while input() != 'quit':
    polygon = []
    # get user input as array
    for points in input().split('),('):
        points = points.replace(')', '').replace('(', '')
        polygon.append(tuple(map(int, points.split(','))))

    for i in range(len(polygon)):
        print(i)
