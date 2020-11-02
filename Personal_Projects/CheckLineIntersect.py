# Script to check whether two lines intersect

# Given three points on a line, function checks if point y lies on line connecting points x and z
def onSegment(x, y, z):
    if y[0] <= max(x[0], z[0]) and y[0] >= min(x[0], z[0]) and y[1] <= max(x[1], z[1]) and y[1] >= min(x[1], z[1]):
        return True

    return False

# To find orientation of ordered triplet (p, q, r).
# The function returns following values
# 0 --> all points are colinear
# 1 --> x, y and z oriented clockwise
# 2 --> x, y and z oriented counterclockwise
def orientation(x, y, z):
    val = ((y[1] - x[1]) * (z[0] - y[0])) - ((y[0] - x[0]) * (z[1] - y[1]))

    if (val == 0):
        return 0
    elif (val > 0):
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


while input() != 'quit':
    x1_coords = tuple(int(x1.strip()) for x1 in input().split(','))
    y1_coords = tuple(int(y1.strip()) for y1 in input().split(','))

    x2_coords = tuple(int(x2.strip()) for x2 in input().split(','))
    y2_coords = tuple(int(y2.strip()) for y2 in input().split(','))

    print(x1_coords)

    if checkIntersection(x1_coords, y1_coords, x2_coords, y2_coords) is True:
        print("Yes\n")
    else:
        print("No\n")

