from HW3_Utils import raiseNotDefined, Point
from random import randint
import dudraw
import math 

'''
Programming Project 3 - Convex Hull
Name: Anh Tran
Date: 02/09/25
'''

# Helper functions
# Q1a
def left_turn(a: Point, b: Point, i: Point) -> bool:
    '''
    Calculates the cross product of vectors ab and bi to see if they make a left turn
    a, b, i: points
    Return: True if is left_turn, otherwise False
    '''
    crossProduct = (b.x - a.x) * (i.y - a.y) - (b.y - a.y) * (i.x - a.x)
    return crossProduct > 0  # left turn if cross product > 0, meaning the point is above the line

# Q1b
def value_based_on_line_distance(a: Point, b: Point, p: Point) -> float:
    '''
    Calculates the distance from line ab to point 
    a,b,p: points
    Return: distance from line ab to point
    '''
    # handling case where the value of Point(a) and Point(b) are the same

    v1x = b.x - a.x
    v1y = b.y - a.y
    v2x = p.x - a.x
    v2y = p.y - a.y
    return abs(v1x*v2y - v1y*v2x)
# Q2
def convex_hull(S: list[Point]) -> list[Point]:
    '''
    Calculates the convex hull of a set of points using the brute force method described in class.
    S: list of points
    Return: list of points on the convex hull
    '''
    # get the points and see if the points in on the line.
    # collect all the furthest points to connect
    # return the set unique if there is only three points.
    if len(S) < 3:
        return list(set(S)) 
    
    # initialize hull list of convexHull points.
    hull = []
    for i in range(len(S)): # every points in S list
        for j in range(i + 1, len(S)): # every other points except i in S list
            a, b = S[i], S[j]
            left_count, right_count = 0, 0 # make count for left and right points.

            for k in range(len(S)): # k point is "p" comparing to "i,j" for "a,b".
                if k != i and k != j:
                    p = S[k]
                    if left_turn(a, b, p):
                        left_count += 1
                    # if point P not above a or b, continue
                    elif not left_turn(a, b, p) and not left_turn(b, a, p):
                        continue  # ignore pts on the line
                    else:
                        # else add there in point above
                        right_count += 1

            # if all the points lay on one side, meaning a, b is the highest points. Append a,b
            if left_count == 0 or right_count == 0:
                if a not in hull:
                    hull.append(a)
                if b not in hull:
                    hull.append(b)

    return sorted(hull, key=lambda p: (p.x, p.y))

# Q3a
def quick_hull_start(S: list[Point]) -> list[Point]:
    '''
    Starts calculating the convex hull using QuickHull
    S: list of points
    Return: list of points on the convex hull
    '''
    if not S:
        return []

    # checks for duplicates and remove it.
    # using dictionary key as the list looping will allows unique values correlates to key.
    # after looping through to get the unique values, append all values back to original list.
    unique_points = list({(p.x, p.y): p for p in S}.values())

    # if there is only two points return the point in sorted manner.
    if len(unique_points) <= 2:
        return sorted(unique_points, key=lambda p: (p.x, p.y))  # Return sorted for consistency

    # find the left most and right most points are pts a and b.
    minX = min(unique_points, key=lambda p: p.x)
    maxX = max(unique_points, key=lambda p: p.x)

    # The first line of convexHull 
    hull = [minX, maxX]

    # Partition into two set, right and left
    left_set = [p for p in unique_points if left_turn(minX, maxX, p)]
    right_set = [p for p in unique_points if left_turn(maxX, minX, p)]

    # run the method again to gets convex Hull points,
    quick_hull(left_set, minX, maxX, hull)
    quick_hull(right_set, maxX, minX, hull)

    # return sorted set of points.
    leftmost = min(hull, key=lambda p: (p.x, p.y))
    return sorted(hull, key=lambda p: math.atan2(p.y - leftmost.y, p.x - leftmost.x))


# Q3b
def quick_hull(S: list[Point], a: Point, b: Point, Result: list[Point]):
    '''
    Recursively computes upper hull
    S: list of points
    a, b: poings
    Result: list of points
    Return: No return, the list of points will be given back to QuickHullStart through Result
    '''
    if not S:
        return

    # if there is only one elements 
    if len(S) == 1:
        # if point is not in the results
        if S[0] not in Result:
            Result.append(S[0]) # add the point
        return

    # compute farthest point from line (a, b)
    max_distance = -1 # initialize value
    farthest_point = None

    for p in S:
        # calculate by value of distance line(a,b) with point p
        distance = value_based_on_line_distance(a, b, p)
        if distance > max_distance:
            max_distance = distance
            farthest_point = p # the furthest distance change

    if farthest_point:
        # if the point is not in Result, added it.
        if farthest_point not in Result:
            Result.append(farthest_point)

        # split the set to check left turn again
        left_set_1 = [p for p in S if left_turn(a, farthest_point, p)]
        left_set_2 = [p for p in S if left_turn(farthest_point, b, p)]

        # recursive calls the function to run the list checking.
        quick_hull(left_set_1, a, farthest_point, Result)
        quick_hull(left_set_2, farthest_point, b, Result)


def generate_points(n: int) -> list[Point]:
    '''
    In order to test that your algorithm works, you can randomly generate a set of points.
    You can then use these random points in the draw_hull() function.
    '''
    # creating a list of point randint numbers 0 to 80.
    return [Point(randint(0, 80), randint(0, 80)) for _ in range(n)]

def draw_hull(S: list[Point], CH: list[Point]):
    '''
    In order to test that your algorithm works, use DUDraw for drawing the set of points. 
    You could draw the points with a certain color and then draw the points of the convex hull with a different color and you should be able to verify if your algorithm worked by looking at the output.
    Include a screenshot of your DUDraw canvas in Programming Project 3 - Runtime Analysis
    ''' 
    dudraw.clear()
    
    # Draw all points in black
    dudraw.set_pen_color(dudraw.BLACK)
    for p in S:
        dudraw.filled_circle(p.x, p.y, 2)

    # Ensure the convex hull points are connected in order
    if len(CH) > 1:
        dudraw.set_pen_color(dudraw.BLUE)
        for i in range(len(CH) - 1):
            dudraw.line(CH[i].x, CH[i].y, CH[i + 1].x, CH[i + 1].y)

        # Connect the last point back to the first to complete the hull
        dudraw.line(CH[-1].x, CH[-1].y, CH[0].x, CH[0].y)

    # Draw convex hull points in red
    dudraw.set_pen_color(dudraw.RED)
    for p in CH:
        dudraw.filled_circle(p.x, p.y, 2)
        
def main():
    
    dudraw.set_canvas_size(800,800)
    dudraw.set_x_scale(-10,100)
    dudraw.set_y_scale(-10,100)
    num_points = 20  
    points = generate_points(num_points)

    brute_force_hull = convex_hull(points)
    quick_hull_result = quick_hull_start(points)

    print("Brute-force Convex Hull Points:")
    for p in brute_force_hull:
        print(f"({p.x}, {p.y})")

    print("\nQuickHull Convex Hull Points:")
    for p in quick_hull_result:
        print(f"({p.x}, {p.y})")

    draw_hull(points, quick_hull_result)
    dudraw.show(float("inf"))

if __name__ == "__main__":
    main()